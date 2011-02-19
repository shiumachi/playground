#!/usr/bin/python
import itertools

def starting_at_five():
    value = raw_input().strip()
    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        value = raw_input().strip()

