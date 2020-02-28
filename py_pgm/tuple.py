#A tuple is a collection which is ordered and unchangeable.
# In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])#access the members
for x in thistuple:#loops
  print(x)
if "apple" in thistuple:#in operator
  print("Yes, 'apple' is in the fruits tuple")
print(len(thistuple))
#thistuple[3] = "orange" # This will raise an error
print(thistuple)
#del thistuple(0)#not possible
#del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)#tuple constructor
tuple = (1, 3, 7, 8, 7, 5, 4, 6, (8, 5))
print (tuple[1:])
print (tuple[0:1])
print (tuple)
print (tuple + tuple)
print (tuple * 3)
print (type(tuple))
#tuple[2] = "hi"   #error
# code to test slicing
print(tuple[1:])
print(tuple[::-1])
print(tuple[2:4])
print(tuple[8][1])

x = tuple.count(5)
print(x)#2
y = tuple.index(8)#Search for the first occurrence of the value 8, and return its position
print(y)
#The index() method raises an exception if the value is not found.
#z=tuple.index(0)
#print(z)
#tuple.clear()#no clear method

t=(1,2,3,4)
u=(1,8,9)
p=(t+u)
print(p)

