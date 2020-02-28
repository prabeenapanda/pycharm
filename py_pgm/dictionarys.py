thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)
print(len(thisdict))
x = thisdict["model"]#to get the value
print(x)
y = thisdict.get("model")#using get same if not there it won't return error
print(y)
thisdict["year"] = 2018#change value
print(thisdict)
print(list(thisdict)) #['brand', 'model', 'year']
print(set(thisdict)) #{'model', 'year', 'brand'}
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])
print(thisdict.values()) #dict_values(['Ford', 'Mustang', 2018])
print(thisdict.items()) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
for x in thisdict:
  print(x)#loop to get keys
for x in thisdict:
  print(thisdict[x])#loop to get values
for x in thisdict.values():
  print(x)#using values same
for x, y in thisdict.items():
  print(x, y)#to get both key and value using item
if "model" in thisdict:
  print("Yes, 'model' is there")
thisdict["color"] = "red"
print(thisdict)#add item
thisdict.pop("model")
print(thisdict)#delete the given value
thisdict.popitem()
print(thisdict)#delete the last inserted value
del thisdict["brand"]
print(thisdict)#delete given value
#del thisdict#delete the dict
#print(thisdict) #this will cause an error
thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
mydict = thisdict.copy()#copy using copy method
print(mydict)
dic = dict(thisdict)#copy without using copy
print(dic)
thisdict.clear()#{}
print(thisdict)
thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
x = ('key1', 'key2', 'key3')
y = 0
thisdic= dict.fromkeys(x, y)
print(thisdic)
thisdi= dict.fromkeys(x)
print(thisdi)#if u dont provide values it will print none
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.items()#givs items
print(x)
y = car.keys()#gives keys
print(y)
z = car.values()#gives values
print(z)
car.update({"color": "White"})#add the value
print(car)
x = car.setdefault("color", "white")#Get the value of the "color" item,
# if the "color" item does not exist, insert "color" with the value "white
print(x)
a={1:'p',2:'q',1:'r'}
print(a)#{1: 'r', 2: 'q'}
print(a[1])#r
#b={3:"pp",4:"qq"}
#c={a+b}  not possible
#print(c)