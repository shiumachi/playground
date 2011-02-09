#/usr/bin/python

class WhatFor(object):

    @classmethod
    def it(cls):
        print ('work with %s' % cls)

    @staticmethod
    def uncommon():
        print 'I could be a global function'

if __name__=='__main__':
    this_is = WhatFor()
    this_is.it()
    this_is.uncommon()
