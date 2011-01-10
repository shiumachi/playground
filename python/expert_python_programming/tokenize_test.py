#!/usr/bin/python
import tokenize

reader = open('tokenize_test.py').readline
tokens = tokenize.generate_tokens(reader)

for i in xrange(10):
    print next(tokens)
