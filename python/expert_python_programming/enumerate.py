#!/usr/bin/python

def _treatment(pos, element):
    return '%d: %s' % (pos, element)

seq = ['one', 'two', 'three']
seq2 = [_treatment(i,el) for i, el in enumerate(seq)]
    
print seq2

