#!/usr/bin/python
import itertools

def with_head(iterable, headsize=1):
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)), b

if __name__=='__main__':
    seq = xrange(10)
    print with_head(seq)
    print with_head(seq, 4)
