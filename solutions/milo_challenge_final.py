#!/usr/bin/env python

########################
#
# https://www.codeeval.com/public_sc/48/
#
# Challenge Description 
#
# Our marketing department has just negotiated a deal with several local merchants
# that will allow us to offer exclusive discounts on various products to our 
# top customers every day. The catch is that we can only offer each product 
# to one customer and we may only offer one product to each customer.
#
# Each day we will get the list of products that are eligible for these special 
# discounts. We then have to decide which products to offer to which of our customers.
# Fortunately, our team of highly skilled statisticians has developed an amazing mathematical 
# model for determining how likely a given customer is to buy an offered product by calculating
# what we call the "suitability score" (SS). The top-secret algorithm to calculate the SS 
# between a customer and a product is this:
# 
# 1. If the number of letters in the product's name is even then the SS 
# is the number of vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5.
# 
# 2. If the number of letters in the product's name is odd then the SS 
# is the number of consonants in the customer's name.
#
# 3. If the number of letters in the product's name shares any
# common factors (besides 1) with the number of letters in the customer's name
# then the SS is multiplied by 1.5.
# 
# Your task is to implement a program that assigns each customer a product to be offered 
# in a way that maximizes the combined total SS across all of the chosen offers. Note that
# there may be a different number of products and customers. You may include code from 
# external libraries as long as you cite the source.
#
############################



# This solution contains Munkres class from "http://github.com/bmc/munkres/"

# import 
import sys
import string

MAXIMUM = 10000
VOWELS = 'aeiouy'

class Match:
    """
    Match products with customers to get the maximal sum of SS.
    """
    def __init__(self, line):
        """Initialization"""
        self.line = line
        self.products = []
        self.customers = []
        self.SS_matrix = []

    def get_list(self):
        """Get products and customers list"""
        L = self.line.split(";")
        self.customers = [ self.__letters(name) for name in L[0].split(",")]
        self.products = [ self.__letters(name) for name in L[1].split(",")]

    def get_SS_matrix(self):
        """Get SS matrix composed by SS between any one of products and customers """
        matrix = []
        for product in self.products:
            matrix.append([ self.__calculate_SS(product,customer) for customer in self.customers])
        self.SS_matrix = matrix
        
    def get_matrix(self):
        """Convert calculating maximal sum of SS to minmial sum of (MAXIMUM - SS)"""
        matrix = []
        for row in self.SS_matrix:
            matrix.append([ MAXIMUM-value for value in row])
        return matrix
        
    def get_biggest_SS(self):
        """Get the maximal sum of SS by using Munkres algorithm"""
        self.get_list()
        self.get_SS_matrix()
        
        matrix = self.get_matrix()
        m = Munkres()
        indexes = m.compute(matrix)    
        total = 0
        for row, column in indexes:
            value = self.SS_matrix[row][column]
            total += value
        return total
        
    def __letters(self,name):
        """Remove non-letters from string and convert to lowercase"""
        return ''.join([ x.lower() for x in name if x in string.letters])

    def __vowels(self,name):
        """Count the number of vowels in string"""
        count = 0
        for c in name:
            if c in VOWELS:
                count += 1
        return count
        
    def __common_factor(self,a,b):
        """Check 2 integers have common factors or not"""
        for i in range(2, min(a,b)+1):
            if a%i == 0 and b%i == 0:
                return True
        return False 

    def __calculate_SS(self,product,customer):
        """Calculat the SS between a product and a customer"""
        product_letters = len(product)
        customer_letters  = len(customer)
        vowels = self.__vowels(customer)
        consonants = customer_letters - vowels

        SS = vowels*1.5 if product_letters%2 == 0 else consonants

        if self.__common_factor(product_letters,customer_letters):
            SS = SS*1.5

        return SS


class Munkres:
    """
    Calculate the Munkres solution to the classical assignment problem.
    See the module documentation for usage.
    """

    def __init__(self):
        self.C = None
        self.row_covered = []
        self.col_covered = []
        self.n = 0
        self.Z0_r = 0
        self.Z0_c = 0
        self.marked = None
        self.path = None

    def pad_matrix(self, matrix, pad_value=0):
        """
        Pad a possibly non-square matrix to make it square.
        """
        max_columns = 0
        total_rows = len(matrix)

        for row in matrix:
            max_columns = max(max_columns, len(row))

        total_rows = max(max_columns, total_rows)

        new_matrix = []
        for row in matrix:
            row_len = len(row)
            new_row = row[:]
            if total_rows > row_len:
                # Row too short. Pad it.
                new_row += [0] * (total_rows - row_len)
            new_matrix += [new_row]

        while len(new_matrix) < total_rows:
            new_matrix += [[0] * total_rows]

        return new_matrix

    def compute(self, cost_matrix):
        """
        Compute the indexes for the lowest-cost pairings between rows and
        columns in the database. Returns a list of (row, column) tuples
        that can be used to traverse the matrix.
        """
        self.C = self.pad_matrix(cost_matrix)
        self.n = len(self.C)
        self.original_length = len(cost_matrix)
        self.original_width = len(cost_matrix[0])
        self.row_covered = [False for i in range(self.n)]  
        self.col_covered = [False for i in range(self.n)]
        self.Z0_r = 0
        self.Z0_c = 0
        self.path = self.__make_matrix(self.n * 2, 0)
        self.marked = self.__make_matrix(self.n, 0)

        done = False
        step = 1

        steps = { 1 : self.__step1,
                  2 : self.__step2,
                  3 : self.__step3,
                  4 : self.__step4,
                  5 : self.__step5,
                  6 : self.__step6 }

        while not done:
            try:
                func = steps[step]
                step = func()
            except KeyError:
                done = True

        # Look for the starred columns
        results = []
        for i in range(self.original_length):
            for j in range(self.original_width):
                if self.marked[i][j] == 1:
                    results += [(i, j)]

        return results

    def __copy_matrix(self, matrix):
        """Return an exact copy of the supplied matrix"""
        return copy.deepcopy(matrix)

    def __make_matrix(self, n, val):
        """Create an *n*x*n* matrix, populating it with the specific value."""
        matrix = []
        for i in range(n):
            matrix += [[val for j in range(n)]]
        return matrix

    def __step1(self):
        """
        For each row of the matrix, find the smallest element and
        subtract it from every element in its row. Go to Step 2.
        """
        C = self.C
        n = self.n
        for i in range(n):
            minval = min(self.C[i])
            # Find the minimum value for this row and subtract that minimum
            # from every element in the row.
            for j in range(n):
                self.C[i][j] -= minval

        return 2

    def __step2(self):
        """
        Find a zero (Z) in the resulting matrix. If there is no starred
        zero in its row or column, star Z. Repeat for each element in the
        matrix. Go to Step 3.
        """
        n = self.n
        for i in range(n):
            for j in range(n):
                if (self.C[i][j] == 0) and \
                   (not self.col_covered[j]) and \
                   (not self.row_covered[i]):
                    self.marked[i][j] = 1
                    self.col_covered[j] = True
                    self.row_covered[i] = True

        self.__clear_covers()
        return 3

    def __step3(self):
        """
        Cover each column containing a starred zero. If K columns are
        covered, the starred zeros describe a complete set of unique
        assignments. In this case, Go to DONE, otherwise, Go to Step 4.
        """
        n = self.n
        count = 0
        for i in range(n):
            for j in range(n):
                if self.marked[i][j] == 1:
                    self.col_covered[j] = True
                    count += 1

        if count >= n:
            step = 7 # done
        else:
            step = 4

        return step

    def __step4(self):
        """
        Find a noncovered zero and prime it. If there is no starred zero
        in the row containing this primed zero, Go to Step 5. Otherwise,
        cover this row and uncover the column containing the starred
        zero. Continue in this manner until there are no uncovered zeros
        left. Save the smallest uncovered value and Go to Step 6.
        """
        step = 0
        done = False
        row = -1
        col = -1
        star_col = -1
        while not done:
            (row, col) = self.__find_a_zero()   
            if row < 0:
                done = True
                step = 6
            else:
                self.marked[row][col] = 2
                star_col = self.__find_star_in_row(row)
                if star_col >= 0:
                    col = star_col
                    self.row_covered[row] = True
                    self.col_covered[col] = False
                else:
                    done = True
                    self.Z0_r = row
                    self.Z0_c = col
                    step = 5

        return step

    def __step5(self):
        """
        Construct a series of alternating primed and starred zeros as
        follows. Let Z0 represent the uncovered primed zero found in Step 4.
        Let Z1 denote the starred zero in the column of Z0 (if any).
        Let Z2 denote the primed zero in the row of Z1 (there will always
        be one). Continue until the series terminates at a primed zero
        that has no starred zero in its column. Unstar each starred zero
        of the series, star each primed zero of the series, erase all
        primes and uncover every line in the matrix. Return to Step 3
        """
        count = 0
        path = self.path
        path[count][0] = self.Z0_r
        path[count][1] = self.Z0_c
        done = False
        while not done:
            row = self.__find_star_in_col(path[count][1])
            if row >= 0:
                count += 1
                path[count][0] = row
                path[count][1] = path[count-1][1]
            else:
                done = True

            if not done:
                col = self.__find_prime_in_row(path[count][0])
                count += 1
                path[count][0] = path[count-1][0]
                path[count][1] = col

        self.__convert_path(path, count)
        self.__clear_covers()
        self.__erase_primes()
        return 3

    def __step6(self):
        """
        Add the value found in Step 4 to every element of each covered
        row, and subtract it from every element of each uncovered column.
        Return to Step 4 without altering any stars, primes, or covered
        lines.
        """
        minval = self.__find_smallest()
        for i in range(self.n):
            for j in range(self.n):
                if self.row_covered[i]:
                    self.C[i][j] += minval
                if not self.col_covered[j]:
                    self.C[i][j] -= minval
        return 4

    def __find_smallest(self):
        """Find the smallest uncovered value in the matrix."""
        minval = sys.maxint
        for i in range(self.n):
            for j in range(self.n):
                if (not self.row_covered[i]) and (not self.col_covered[j]):
                    if minval > self.C[i][j]:
                        minval = self.C[i][j]
        return minval

    def __find_a_zero(self):
        """Find the first uncovered element with value 0"""
        row = -1
        col = -1
        i = 0
        n = self.n
        done = False

        while not done:
            j = 0
            while True:
                if (self.C[i][j] == 0) and \
                   (not self.row_covered[i]) and \
                   (not self.col_covered[j]):
                    row = i
                    col = j
                    done = True
                j += 1
                if j >= n:
                    break
            i += 1
            if i >= n:
                done = True

        return (row, col)

    def __find_star_in_row(self, row):
        """
        Find the first starred element in the specified row. Returns
        the column index, or -1 if no starred element was found.
        """
        col = -1
        for j in range(self.n):
            if self.marked[row][j] == 1:
                col = j
                break

        return col

    def __find_star_in_col(self, col):
        """
        Find the first starred element in the specified row. Returns
        the row index, or -1 if no starred element was found.
        """
        row = -1
        for i in range(self.n):
            if self.marked[i][col] == 1:
                row = i
                break

        return row

    def __find_prime_in_row(self, row):
        """
        Find the first prime element in the specified row. Returns
        the column index, or -1 if no starred element was found.
        """
        col = -1
        for j in range(self.n):
            if self.marked[row][j] == 2:
                col = j
                break

        return col

    def __convert_path(self, path, count):
        for i in range(count+1):
            if self.marked[path[i][0]][path[i][1]] == 1:
                self.marked[path[i][0]][path[i][1]] = 0
            else:
                self.marked[path[i][0]][path[i][1]] = 1

    def __clear_covers(self):
        """Clear all covered matrix cells"""
        for i in range(self.n):
            self.row_covered[i] = False
            self.col_covered[i] = False

    def __erase_primes(self):
        """Erase all prime markings"""
        for i in range(self.n):
            for j in range(self.n):
                if self.marked[i][j] == 2:
                    self.marked[i][j] = 0


if __name__ == "__main__":
    test_cases = open(sys.argv[1],'r')
    for test in test_cases :
        m = Match(test)
        biggest_SS = m.get_biggest_SS()
        print '%.2f' % biggest_SS