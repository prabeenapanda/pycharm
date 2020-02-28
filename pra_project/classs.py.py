# What is a class? write an example program to demonstrate class.

# A class is a blue print to create object, which defines the methods and member variables for the object.


class MyClass:

    classVar = 'I am class variable'

    def __init__(self, var1, var2):
        print('Object Created')
        self.var1 = var1
        self.var2 = var2
        print(f'Param1 = {var1}, Param2 = {var2}')

    def func1(self, param1, param2):
        print('Hey!! I am funct1 and taktes two parameters', param1, param2)

    @classmethod
    def func2(cls):
        print('I am class method')

    @staticmethod
    def func3():
        print('I am static method')


obj1 = MyClass(5,10)
print(obj1.classVar)
print(MyClass.classVar)
print("-----------------------------------------------")
obj1.classVar = 6
print(obj1.classVar)
print(MyClass.classVar)
print("-----------------------------------------------")
print(obj1.var1)

obj1.func2()
MyClass.func2()

obj1.func3()
MyClass.func3()

print("-----------------------------------------------")

obj1.func1(1,2)
MyClass.func1(obj1,8,9)