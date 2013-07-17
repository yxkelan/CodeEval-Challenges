#
# Challenge Description:
#  
# Write a program to read a multiple line text file and write the 'N' longest lines to stdout. 
# Where the file to be read is specified on the command line.
#
#

# ####  Version 1 ####  

 def longestLines(N, lines):

    newLines = sorted(lines, key = len, reverse = True)

    for i in range(N):
       print newLines[i]


# #### Version 2 ####
#  Not sort all the list, only sort the N longest list.  It will save more time,
#  however, it will cost more memory. This extra cost comes from the findNthElements recursion. 

def longestLines(N, lines):

    rest = len(lines) - N - 1
    findNthElements(rest, lines, 0, len(lines)-1)

    newLines = sorted(lines[rest+1:], key=len, reverse=True)

    for line in newLines:
        print line


def findNthElements(N, A, left, right):

    n = partition( A, left, right)
    if n == N:
        return
    elif n < N:
        return  findNthElements(N, A, n+1,right)
    else:
        return findNthElements(N, A, left,n-1)
    

def partition( A, left, right):
    if left >= right:
        return left

    pivot = len(A[right])
    i = left
    j = left
    for i in range(left, right):
        if len(A[i]) < pivot:
            A[i], A[j] = A[j], A[i]
            j += 1
    A[right], A[j] = A[j], A[right]
    return j


def main():
    test_cases = open(sys.argv[1], 'r')
    i = 0
    lines = []
    for test in test_cases:
        if i == 0:
            N = int(test.strip())
            i += 1
        else:
            test = test.strip()
            if test: lines.append(test)

    longestLines(N, lines)
    test_cases.close()

if __name__ == "__main__":
    main()