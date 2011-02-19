#/usr/bin/python
import functools

def mydecorator(function):
    @functools.wraps(function)
    def _mydecorator(*args, **kw):
        """decorator's docstring"""
        print "before the function is called"
        res = function(*args, **kw)
        print "after the function is called"
        return res
    return _mydecorator

@mydecorator
def my_function(arg):
    """my docstring"""
    return arg

if __name__=='__main__':
    print "my function is %s" % my_function.func_name
    print "my docstring is %s" % my_function.func_doc
    print help(my_function)
    print my_function("test")
    
