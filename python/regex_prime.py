#!/usr/bin/python
# usage: python regex_prime.py [N]
# where N is natural number.
#
# list prime numbers which is less than N,
# using regexp instead of any other usual
# prime sieve algorithm.
#

import sys,re

r = re.compile('^(..+)\\1+$')
N = int(sys.argv[1])

for i in xrange(2,N):
    if not r.match('x' * i):
        print i 

