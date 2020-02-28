def my_decorator(func):
    def wrapper(a,b):
        # a=int(input("enter a:"))
        # b=int(input("enter b:"))
        if a>b:
             func(a,b)
        else:
             func(b,a)
    return wrapper

@my_decorator
def sub(a,b):
    print(a-b)
sub(12,3)

# we can not write multiple decorator in the main function but u can use 1 decorator in multiple
#main fun with different names.