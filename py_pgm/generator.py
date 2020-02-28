# A Python program to demonstrate use of generator object with next()
#generators are iterator but not viceversa.

# A generator function
def GeneratorFun():
	yield 1
	print("hello")
	yield 2
	yield 3

# x is a generator object

x = GeneratorFun()

# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))
def fibon(n):
		a = b = 1
		result = []
		for i in range(n):
			result.append(a)
			a, b = b, a + b
		return result
print(fibon(5))



#we cwn iterate through generator object only but can't through generator funs
def fun():
	yield 1
	yield 2
	yield 3
g=fun()#many objects can be created from 1 generator function
f=fun()
print(g) #gines memory address of g
print(f) #gives memory address of f (different mem add)
for k in g: #here g is generator object
	print(k) #1 2 3
for k in fun: #error "function" oblect is not callable because it is generator function
	print(k)
for k in  fun():
	print(k) #1 2 3

#generator comprehension
gf=(k for k in range(10))# here gf is a generator object
for k in gf:#so gf can be iterable now
	print(k)


#chain generator
a=(k+2 for k in range(10))#here a is a generator object
b=(k+10 for k in a) #now a is converted to an iterable
for k in b:
	print(k) #1 to 21


#generator doesn't do much just define the behaviour
