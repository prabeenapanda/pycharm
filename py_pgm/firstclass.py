def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am Prabeena")
    print(greeting)
greet(shout)
greet(whisper)



def hello(name):
    return "hello "+name
def bye(name):
    return "bye "+name
def great(fun):
    greating=fun("Prabeena")
    print(greating)
great(hello)
great(bye)



def foo(x,y):
    return x+y+1
def boo(fut):
    return fut
print(boo(foo(3,4)))

def foo(bar,xar):
    return bar + xar + 1

def call_foo_with_arg(my_func, num1, num2):
    return my_func(num1,num2) # foo(3)

print("Firt class fucntion called :",call_foo_with_arg(foo, 3, 5))  #2n