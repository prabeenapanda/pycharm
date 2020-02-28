def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()
f()
#This is the function 'f'
#I am calling 'g' now:
#Hi, it's me 'g'
#Thanks for calling me
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
f(g)
#Hi, it's me 'f'
#I will call 'func' now
#Hi, it's me 'g'
#Thanks for calling me
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__)
f(g)
#Hi, it's me 'f'
#I will call 'func' now
#Hi, it's me 'g'
#Thanks for calling me
#func's real name is g
