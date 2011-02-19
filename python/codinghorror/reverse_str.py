#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) != 2:
    sys.stderr.write("usage: %s string\n" % (sys.argv[0]))
    sys.exit(1)

string = sys.argv[1]

print string[::-1]
    
