#!/usr/bin/python
def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print "ok let's clean"

if __name__=='__main__':
    gen = my_generator()
    print next(gen)
    print gen.throw(ValueError('mean mean mean'))
    print gen.close()
    print next(gen)
        
