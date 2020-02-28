# What is method over loading? write an example program to demonstrate method overloading.
# Methods having same name with diffrent signatire in the same class called method Over loading.
# As the signature of a method is optional in Python, it does not support method over loading.
# However the built in functionas can be overloaded by using magic function associated to the function
# We may define many method of same name and different argument but we can only use the latest method.
#python does not support method overloading.

class Test:
    def m1(self, i:int):
        print(i)

    def m1(self, i:str):
        print("My name is: ", i)

    def product(self, a, b):
        return a*b

    def product(self, a, b, c):
        return a * b * c


test = Test()

test.m1(5)
test.m1("Sanjib")

#test.product(2,3)
test.product(2,3,4)


class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

order = Order(['banana', 'apple', 'mango'], 'Sanjib')
print(len(order))