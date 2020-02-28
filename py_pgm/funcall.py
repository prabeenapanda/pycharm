def hello(a):
    a=10
    print("hello world")
    return a
a=hello
print(a) #memory address
print(id(a))
a=hello(20)
print(a) #output
print(id(a))
#required args
def hi(a):
    print(a)
hi(3) #hi
#default arg
def fun(a,b=0):
    print(a,b)
fun(1) #1 0
fun(1,2) #1 2
#keyword arg
def myfun(a,b):
    print(a,b)
myfun(a=2,b=7)