price = 49
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:.2f} dollars"
print(txt.format(price))
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
x=100


#fstring use "f" or "F" in the bigining of the print statement.
print(f'Temp is {x}')
print(F'Temp is not {x**8:,}')
import math
print(f'{math.sqrt(9)}')


import time
start=time.perf_counter()
print("hi")
x=time.perf_counter()-start
print(x)
