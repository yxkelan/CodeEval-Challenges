#
# Challenge Description:
# Write a program to determine the Mth to last element of a list.
# Input sample:
# The first argument will be a text file containing a series of space
# delimited characters followed by an integer representing a index into
# the list(1 based), one per line. e.g. 
# a b c d 4
# e f g h 2
#


def mthToLastElement(s):
    s_list = s.strip().split()
    n = int(s_list[-1])
    if n < len(s_list): print s_list[-1-n]

    return


##  Iterate string instead of list, it is fast, but take more spaces. 
def mthToLastElement2(s):
    s = s.strip()
    length = (len(s)-1)/2
    n = int(s[-1])
    if n <= length:
        print s[-1-n*2]

    return

def main():
    import sys
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        #mthToLastElement(test)
        mthToLastElement2(test)
    test_cases.close()

if __name__ == "__main__":
    main()
