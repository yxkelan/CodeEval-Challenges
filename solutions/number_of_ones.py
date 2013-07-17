#
# Challenge Description:
# 
# Write a program to determine the number of 1 bits in 
# the internal representation of a given integer.

# Input sample:
#
# 10
# 22
# 56
#
# Output sample:
#
# Print to stdout, the number of ones in the binary form of each number.
# e.g.
# 2
# 3
# 3
#


import sys

def numOfOnes(s):
    dec_number = int(s.strip())

    ones = 0

    while dec_number > 0:
        rem  = dec_number % 2
        dec_number = dec_number // 2
        if rem:
            ones += 1

    return ones

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print numOfOnes(test)

    test_cases.close()

if __name__ == '__main__':
    main()