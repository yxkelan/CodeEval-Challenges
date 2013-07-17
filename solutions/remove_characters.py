#
# Challenge Description:
#
# Write a program to remove specific characters from a string.
#
# Input sample:
#
# The first argument will be a text file containing an input 
# string followed by a comma and then the characters that need to be scrubbed. e.g. 
#
# how are you, abc
# hello world, def
#
# Output 
#
# how re you
# hllo worl

import sys


def process( s ):
    s_list = s.split(',')
    return s_list[0].strip(), s_list[1].strip()

def removeCharacters( Input ):
    A, B = process(Input)

    chars = { v:1 for v in B}
    newA = [ v for v in A  if not v in B]
    return ''.join(newA)

def main():

    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print removeCharacters(test)
    test_cases.close()


if __name__ == "__main__":
    main()