#!/usr/bin/python
import multitask

def coroutine_1():
    for i in xrange(10):
        print "coroutine_1"
        yield i

def coroutine_2():
    for i in xrange(10):
        print "coroutine_2"
        yield i


if __name__=='__main__':
    multitask.add(coroutine_1())
    multitask.add(coroutine_2())
    multitask.run()
        
