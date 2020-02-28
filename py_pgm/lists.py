#List is a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])#apple
print (thislist[3:])
print (thislist[0:2])
print (thislist + thislist)
print (thislist * 3)
thislist[1] = "blackcurrant"#we can not give more then range here more then 2
print(thislist)#change item value
for x in thislist:#loop
  print(x)
if "apple" in thislist:#in operator
  print("Yes, 'apple' is in the fruits list")
print(len(thislist))#3
thislist.append("orange")#adds at the end
print(thislist)
thislist.insert(1, "orange")#add item at specific location
print(thislist)
thislist.remove("apple")#removes specified item
print(thislist)
thislist.pop()# removes the specified index, (or the last item if index is not specified)
print(thislist)
del thislist[0]#delete item at specified location
print(thislist)
del thislist#deletes whole list
#print(thislist)#error
thislist = ["apple", "banana", "cherry"]
thislist.clear()#empties the list
print(thislist)#[]
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()#copy list
#mylist = list(thislist)   {or to copy}
print(mylist)
hislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(hislist)#list constructor
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)#2
print(x)
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)#add 1 list to another list
print(fruits)
y=fruits.index("cherry")#gives the index value
print(y)
fruits.reverse()
print(fruits)
cars.sort()#sort the list alphabatically
print(cars)
cars.sort(reverse=True)
print(cars)#sort in descending by default reverse is false
#Sort the list by the length of the values
def myFunc(e):#fun to give the length
  return len(e)

car = ['Ford', 'Mitsubishi', 'BMW', 'VW']
car.sort(key=myFunc)
print(car)
#Sort the list by the length of the values and reversed
car.sort(reverse=True, key=myFunc)
print(car)
l=[1,2,3,4]
i=[1,6,8,9]
s=[l+i] #[[1, 2, 3, 4, 1, 6, 8, 9]]
print(s)
t=l+i
print(t) #[1, 2, 3, 4, 1, 6, 8, 9]




