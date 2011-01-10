#!/usr/bin/python
def power(values):
    for value in values:
        print "powering %s" % (value)
        yield value

def adder(values):
    for value in values:
        print "adding to %s" % (value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

elements = [1, 4, 7, 9, 12, 19]
res = adder(power(elements))

for i in xrange(10):
    try:
        print next(res)
    except StopIteration:
        print "error: array is empty"
    
        
