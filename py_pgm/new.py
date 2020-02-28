# Method __new__ is responsible to create instance, so you can use this method to customize object creation
# . Typically method __new__ will return the created instance object reference.
# Method __init__ will be called once __new__ method completed execution.
# __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.
class Foo(object):
    def __new__(cls, *args, **kwargs):
        print("Creating Instance")
        instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass