#!/bin/python3

# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'thisisapasswordofemail!@#1231',
             'blog': 'thisisthepasswordofblog',
             'luggage': '123445'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name
