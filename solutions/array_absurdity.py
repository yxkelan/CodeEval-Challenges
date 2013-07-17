#
# Challenge Description:
#
# Imagine we have an immutable array of size N 
# which we know to be filled with integers ranging 
# from 0 to N-2, inclusive. Suppose we know that 
# the array contains exactly one duplicated entry 
# and that duplicate appears exactly twice. 
# Find the duplicated entry. (For bonus points, 
# ensure your solution has constant space and time proportional to N)
#
# Input sample:
#
# Your program should accept as its first argument a path to a filename. 
# Each line in this file is one test case. Ignore all empty lines. 
# Each line begins with a positive integer(N) i.e. the size of the array, 
# then a semicolon followed by a comma separated list of positive numbers
# ranging from 0 to N-2, inclusive. i.e eg.
# 
# 5;0,1,2,3,0
# 20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14
# Output sample:
#
# Print out the duplicated entry, each one on a new line eg
#
# 0
# 4
#

import sys

def arrayAbsurdity(s):
    N, numbers = process(s)
    #return N, numbers

    sum_of_N =  (N-1)*(N-2)/2
    sum_of_numbers = 0
    for v in numbers:
        sum_of_numbers += int(v.strip())

    return sum_of_numbers - sum_of_N

def process(s):
    s_list = s.split(';')
    numbers = s_list[1].split(',')
    return int(s_list[0].strip()), numbers

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if test: print arrayAbsurdity(test)
    test_cases.close()

if __name__ == "__main__":
    main()

