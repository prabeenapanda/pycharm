# What is operator overoloading? write an example program to provide + operator support to two instances of particular class.
# Operator overloading is a technique by which operators are implemented in user-defined types/ classes with customized logic.


# class Order:
#      def __init__(self, cart, customer):
#          self.cart = list(cart)
#          self.customer = customer
#
#      def __add__(self, other):
#          new_cart = self.cart.copy()
#          new_cart.append(other)
#          return Order(new_cart, self.customer)
#
# order = Order(['banana', 'apple'], 'Real Python')
#
# print((order + 'orange').cart)
# print(order.cart)
#
# order = order + 'mango'
# print(order.cart)



class Complex:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return Complex(self.num1 + other.num1, self.num2 + other.num2)

    def __str__(self):
        return f'({self.num1}, {self.num2})'


obj1 =  Complex(1, 2)
obj2 =  Complex(3, 4)


print(obj1 + obj2)

print((obj1 + obj2).num1)
