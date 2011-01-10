#!/usr/bin/python
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

if __name__=='__main__':
    fib = fibonacci()
    for i in xrange(10):
        print next(fib)
        
