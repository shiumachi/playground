#!/usr/bin/python
import os
import sys

FILENAME='./int_list.txt'

def sum_int(filename):
    try:
        f = open(filename, 'r')
    except:
        sys.exit("file open error")

    res = 0
        
    for line in f:
        try:
            x = int(line.strip())
        except:
            sys.stderr.write("error: %s is not a number\n" % x)
            continue
        res += x

    f.close()

    return res

if __name__=='__main__':
    print sum_int(FILENAME)


