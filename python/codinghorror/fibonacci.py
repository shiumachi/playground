#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def usage():
    sys.stderr.write("usage: %s num (num > 0)\n" % (sys.argv[0]))
    

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

if not sys.argv[1].isdigit():
    usage()
    sys.exit(2)

num = int(sys.argv[1])

if num < 0:
    usage()
    sys.exit(3)

if num == 1:
    print "1st fibonacci number: 1"
    sys.exit(0)
elif num == 2:
    print "2nd fibonacci number: 1"
    sys.exit(0)
elif num == 3:
    print "3rd fibonacci number: 2"
    sys.exit(0)

a, b = 1, 2

for i in xrange(4, num+1):
    a, b = b, a+b

print "%dth fibonacci number: %d" % (num, b)
