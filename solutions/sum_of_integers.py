#
# Challenge Description:
# 
# Write a program to determine the largest sum of contiguous integers in a list.
# 
# Input sample:
#
# The first argument will be a text file containing a comma separated list of integers, one per line. e.g. 
#
# -10, 2, 3, -2, 0, 5, -15
# 2,3,-2,-1,10
# Output sample:
#
# Print to stdout, the largest sum. In other words, 
# of all the possible contiguous subarrays for a given array, 
# find the one with the largest sum, and print that sum.
# e.g.
#
# 8
# 12
#

import sys

def sumOfIntegers(s):
    numbers = process(s)

    maxSum = numbers[0]
    last = numbers[0]
    for i in range(1,len(numbers)):
        if last + numbers[i] > numbers[i]:
            last += numbers[i]
        else:
            last = numbers[i]
        maxSum = last if last > maxSum else maxSum

    return maxSum


def process(s):
    s_list = s.split(",")
    A = [ int(v.strip()) for v in s_list]
    return A

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print sumOfIntegers(test)
        #print process(test)
    test_cases.close()

if __name__ == "__main__":
    main()