#
# Challenge Description:
#
# The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet. 
# Such sentences are called pangrams. You are to write a program, which takes a sentence, 
# and returns all the letters it is missing (which prevent it from being a pangram). 
# You should ignore the case of the letters in sentence, and your return should be all lower case letters,
# in alphabetical order. You should also ignore all non US-ASCII characters.
# In case the input sentence is already a pangram, print out the string NULL

# Input sample:

# A quick brown fox jumps over the lazy dog
# A slow yellow fox crawls under the proactive dog
# Output sample:

# Print out all the letters each string is missing in lowercase, alphabetical order .e.g.
#
# NULL
# bjkmqz
#

import sys


ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def pangram(s):
    s = s.strip()
    start = ord('a')
    chars = [0] * 26

    # No necessary to add a length check if it is equal to 0
    # len() takes O(n), the missings also take O(n). Usually, the string is not empty,
    # check length will cost more time.

    for c in s:
        index = ord(c.lower()) - start
        if index > -1  and index < 26 : chars[index] = 1

    missings = [ ALPHABET[i] for i in range(26) if chars[i] == 0]

    return ''.join(missings) if missings else "NULL"

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print pangram(test)
    test_cases.close()

if __name__ == "__main__":
    main()
