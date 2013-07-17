#
# Challenge Description:
#
# You are given a sorted array of positive integers and a number 'X'. 
# Print out all pairs of numbers whose sum is equal to X. 
# Print out only unique pairs and the pairs should be in ascending order
# 
# Input sample:
# Your program should accept as its first argument a filename. 
# This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon. 
# Ignore all empty lines. If no pair exists, print the string NULL eg.
# 
# 1,2,3,4,6;5
# 2,4,5,6,9,11,15;20
# 1,2,3,4;50
#
# Output sample:
# Print out the pairs of numbers that equal to the sum X. 
# The pairs should themselves be printed in sorted order 
# i.e the first number of each pair should be in ascending order .e.g.
# 
# 1,4;2,3
# 5,15;9,11
# NULL
#

import sys

def numberPairs(s):
    numbers, X = process(s)
    i = 0
    j = len(numbers)-1
    pairs = []
    while i < j:
        A = numbers[i]
        B = numbers[j]
        if A + B == X:
            pairs.append("%s,%s" % (A , B))
            i += 1
        elif A + B < X:
            i += 1
        else: 
            j -= 1

    return ";".join(pairs) if len(pairs) > 0 else "NULL"
        
def process(s):
    s_list = s.strip().split(';')
    part1 = s_list[0].strip().split(',')
    A = [ int(v.strip()) for v in part1 ]
    B = int(s_list[1].strip())
    return  A, B


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print numberPairs(test)
        #process(test)
    test_cases.close()

if __name__ == "__main__":
    main()