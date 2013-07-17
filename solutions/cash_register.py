#
# Challenge Description:
#
# The goal of this challenge is to design a cash register program. 
# You will be given two float numbers. 
# The first is the purchase price (PP) of the item. 
# The second is the cash (CH) given by the customer. 
# Your register currently has the following bills/coins within it:
#
# 'PENNY': .01,
# 'NICKEL': .05,
# 'DIME': .10,
# 'QUARTER': .25,
# 'HALF DOLLAR': .50,
# 'ONE': 1.00,
# 'TWO': 2.00,
# 'FIVE': 5.00,
# 'TEN': 10.00,
# 'TWENTY': 20.00,
# 'FIFTY': 50.00,
# 'ONE HUNDRED': 100.00
# 
# The aim of the program is to calculate the change that has to be returned to the customer.
#
# Input sample:
#
# Your program should accept as its first argument a path to a filename. 
# The input file contains several lines. Each line is one test case. 
# Each line contains two numbers which are separated by a semicolon. 
# The first is the Purchase price (PP) and the second is the cash(CH) given by the customer. eg.
#
# 15.94;16.00
# 17;16
# 35;35
# 45;50
#
# Output sample:
#
# For each set of input produce a single line of output 
# which is the change to be returned to the customer. 
# In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. 
# For all other cases print the amount that needs to be returned, in terms of the currency values provided. 
# The output should be sorted in highest-to-lowest order (DIME,NICKEL,PENNY). eg.
#
# NICKEL,PENNY
# ERROR
# ZERO
# FIVE
#

import sys
from decimal import Decimal

CURRENCY = ['ONE HUNDRED', 'FIFTY', 'TWENTY', 'TEN', 'FIVE',
            'TWO', 'ONE', 'HALF DOLLAR', 'QUARTER', 'DIME', 'NICKEL', 'PENNY']
VALUE = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]


def cashRegister(s):
    PP, CH = process(s)

    if PP > CH: return "ERROR"
    if PP == CH: return "ZERO"

    #return PP, CH
    changes = round(CH - PP, 2)
    #return changes
    i = 0
    units = len(CURRENCY)
    CL = []

    while i < units and changes > 0:
        if changes >= VALUE[i]:
            CL.append(CURRENCY[i])
            changes = round( changes - VALUE[i], 2)
        else:
            i += 1

    return ','.join(CL)


def process(s):
    s_list = s.strip().split(';')
    return float(s_list[0].strip()), float(s_list[1].strip())


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print cashRegister(test)
    test_cases.close()

if __name__ == "__main__":
    main()
