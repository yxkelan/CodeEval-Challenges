

import sys

def decimalToBinary(s):
    dec_number = int(s.strip())

    binary = []
    while dec_number > 0:
        rem  = dec_number % 2
        binary.append(str(rem))
        dec_number = dec_number // 2
        
    reverse = binary[::-1]

    return "".join(reverse)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print decimalToBinary(test)

    test_cases.close()

if __name__ == '__main__':
    main()