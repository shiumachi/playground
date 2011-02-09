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

table = [[str(i*j) for i in xrange(1, num+1)] for j in xrange(1, num+1)]

for line in table:
    print '\t'.join(line)




