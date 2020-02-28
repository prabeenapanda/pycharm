#import functools
def mydeco(func):
    #@functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("before func")
        func(*args,**kwargs)
        print("after func")
    return wrapper

@mydeco
def hello(n=None):
    print("my name is Prabeena"*n)
hello(2)
