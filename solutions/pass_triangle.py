#
# Challenge Description
#
# By starting at the top of the triangle and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 27.
#
#    5
#   9 6
#  4 6 8
# 0 7 1 5
#5 + 9 + 6 + 7 = 27
# Input sample:
#
# 5
# 9 6
# 4 6 8
# 0 7 1 5
#
# You make also check full input file(pass_triangle2.txt) which will be used for your code evaluation.
#
# Output sample:
#
# The correct output is the maximum sum for the triangle. 
# So for the given example the correct answer would be
#
# 27
# 

import sys

triangle = []
sums = []

def maxSumOfPath():
    getSumOfPath(0, 0, 0)
    return max(sums)

def getSumOfPath(level, index, sumv):
    try:
        v =  triangle[level][index]
    except:
        sums.append(sumv)
        return

    sumv += int(v)
    getSumOfPath(level+1, index, sumv)
    getSumOfPath(level+1, index+1, sumv)
    return


def process(s):
    s_list = s.split()
    triangle.append(s_list)


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if test: process(test)

    print maxSumOfPath()
    test_cases.close()

if __name__ == "__main__":
    main()

