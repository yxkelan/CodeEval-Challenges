#
# Challenge Description:
#
# You are given two strings 'A' and 'B'. 
# Print out a 1 if string 'B' occurs at the end of string 'A'. Else a zero.
#

import sys
import re


def makePattern( s ):
    pattern = re.compile(s+r'$')
    return pattern

def trailingString( Input ):
    A, B = process(Input)
    pattern  = makePattern(B)
    if pattern.search(A):
        return 1
    return 0

def process( s ):
    s_list = s.split(',')
    return s_list[0].strip(), s_list[1].strip()

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print trailingString(test)
    test_cases.close()

if __name__ == "__main__":
    main()