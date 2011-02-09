#!/usr/bin/python
import itertools

def compress(data):
    return ((len(list(group)), name) for name, group in itertools.groupby(data))

def decompress(data):
    return (car * size for size, car in data)
    
if __name__=='__main__':
    print list(compress('get uuuuuuuuuuuuup'))
    compressed = compress('get uuuuuuuuuuuuup')
    print ''.join(decompress(compressed))
