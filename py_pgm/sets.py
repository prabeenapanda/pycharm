#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
#You cannot access items in a set by referring to an index.
for x in thisset:
  print(x)
if "banana" in thisset:
  print("banana is available")
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.
thisset.add("orange")
print(thisset)
thisset.update(["orange", "mango", "grapes"])
print(thisset)
print(len(thisset))
thisset.remove("banana")#removes banana if not available raise error
print(thisset)
thisset.discard("orange")#same as remove but if not available will not raise error
print(thisset)
x = thisset.pop()#removes last item we can not give index value like list here
print(x)#can be anything as unordered
print(thisset)
sets = {"apple", "banana", "cherry"}
sets.clear()
print(sets)#set()  not {}
this = { "banana", "cherry"}
#del this
print(this)#will show error coz deleted
tet = set(("guava","banana","cherry")) # note the double round-brackets
print(tet)
fruits = {"apple", "banana", "cherry"}
c = fruits.copy()#copy set
print(c)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #gives x-y which is available in x but not in y
print(z)
x.difference_update(y)#(x-y)
print(x)#same output just using update
a={1,2,3}
b={2,3,4,5}
print(a[1])
p = a.intersection(b) #gives which is vailable in both x and y
print(p)
a.intersection_update(b)
print(a)#{2,3}
a={1,2,3,4}
b={3,4,5}
r=a.union(b)
print(r)#gives all the element avilable in a and b
#a.union_update(b)#there is no such function use update func for this
print(a)
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)#(x&y)
print(result)
result = x.union(y, z)#(x|y)
print(result)
z = x.isdisjoint(y) #returns true if no item in x present in y else false
print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print(y[::-1])
z = x.issubset(y) #returns true if all element of x present in y
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #(x-y)+(y-x)=(x^y)
print(z)
x.symmetric_difference_update(y)
print(y)
