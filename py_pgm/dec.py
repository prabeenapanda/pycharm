def fun(some):
    def wrap():
        print("pre:hi")
        some()
        print("post:bye")
    return wrap
#@fun
def abc():
    print("Prabeena")
xyz=fun(abc)
print(xyz())

def decorator(dec):
    def wrapper():
        print("hi")
        dec()
        print("bye")
    return wrapper
@decorator
def aaa():
    print("Prabeena")
aaa()
