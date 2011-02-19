#!/usr/bin/python
import sys

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

if __name__=='__main__':
    fib = fibonacci()
    num = int(sys.argv[1])
    for i in xrange(num):
        print next(fib)
        
