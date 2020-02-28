# Python Program illustrate how
# to overload an binary + operator

class A:
	def __init__(self, a):
		self.a = a

	# adding two objects
	def __add__(self, o):
		return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

class complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	# adding two objects
	def __add__(self, other):
		return self.a + other.a, self.b + other.b

	def __str__(self):
		return self.a, self.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)
