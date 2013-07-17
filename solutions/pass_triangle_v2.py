
# This is the optimal one. It stores the intermediate sums to avoid repeating calculation.
# Caluation from bottom to top, it is similar to calculate the longest path from root to leaf. 
# So the time cost will be O(n), and space cost will also be O(n).

import sys

triangle = []
sums = []

def maxSumOfPath():
    length = len(triangle) - 1
    return getMaxSum(0, 0, length)

def getMaxSum(level, index, length):
    if level > length:
        return 0

    if level+1 < length and sums[level+1][index] != -1:
        leftMax = sums[level+1][index]
    else:
        leftMax = getMaxSum(level+1, index, length)

    if level+1 < length and sums[level+1][index+1] != -1:
        rightMax = sums[level+1][index+1]
    else:
        rightMax = getMaxSum(level+1, index+1, length)

    v = triangle[level][index]
    current = leftMax if leftMax >= rightMax else rightMax
    current += v
    sums[level][index] = current

    return current


def process(s):
    s_list = s.split()
    triangle.append([ long(v) for v in s_list])
    sums.append([ -1 for i in range(len(s_list)) ])

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if test: process(test)

    print maxSumOfPath()
    test_cases.close()

if __name__ == "__main__":
    main()