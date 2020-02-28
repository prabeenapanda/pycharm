p="prabeena"
r="prabeena"
q=r
#id(p)=id(r)=id(q)
#dir(p)=dir('')
a="hello World"
print(a)
print(type(a))
print("a[4] = ", a[4])
print("a[6:11] = ", a[6:11])
print("a[6:20:2] = ", a[6:20:2]) #if u give range more then length it will go till the end of the string
#a [5] ='d'  #error as string is immutable

b='hi'
print(b)
print (b*2)
print (a+b)
print(b + "TEST")
#print(a+=b)#the reference from a will be deleted and the new value will be referenced
# as string is immutable nothing happens to the original string only reference changes every time

x = a.capitalize()#1st char as upper
print (x)

x = a.upper().lower()#we can use multiple methodes in one
print(x)

x = a.casefold()#same as lower but more efficient
print(x)

x = b.center(20)#taking up the space of 20 characters, with "hi" in the middle
print(x)

txt = "I love apples, apple are my favorite fruit."
y = txt.count("apple")
print(y) #2
y = txt.count("apple", 10, 24)
print(y) #1

y = txt.endswith(".")
print(y) #true
y = txt.endswith("fruit.", 5, 11)
print(y) #false

x = txt.startswith("I")
print(x)
x = txt.startswith("app", 7, 20)
print(x)

y = txt.find("love")
print(y)
y = txt.find("e", 5, 10)
print(y)
#The find() method is almost the same as the index() method,find method returns -1 if not found
# the only difference is that the index() method raises an exception if the value is not found.
print(txt.find("q"))
#print(txt.index("q")) #error

txt = "For only {price:.2f} dollars!"
print(txt.format(price=87))
txt1 = "My name is {fname}, I'am {age}".format(fname = "John", age = 36)
print(txt1)
txt2 = "My age is {1}, I'am {0}".format("John",36)
print(txt2)
txt3 = "My name is {}, I'am {}".format("John",36)
print(txt3)

txt = "Company12"
x = txt.isalnum()
print(x)#true
txt = "Company 12"
x = txt.isalnum()
print(x)#false

txt = "CompanyX"
x = txt.isalpha()
print(x) #true

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal()) #true
print(b.isdecimal()) #false

txt = "50800"
x = txt.isdigit()
print(x) #true
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit()) #true
print(b.isdigit()) #true

#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9),
# or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())#true
print(b.isidentifier())#true
print(c.isidentifier())#False
print(d.isidentifier())#false

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())#false
print(b.islower())#true
print(c.islower())#false

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d= "4565678"
print(a.isnumeric())#true
print(b.isnumeric())#true
print(c.isnumeric())#false
print(d.isnumeric())#true

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)#false

txt = "   "
x = txt.isspace()
print(x)#true

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)#true

b = "hello 123"
c = "MY NAME IS PETER"
print(b.isupper())#false
print(c.isupper())#true

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
txt = "banana"
x = txt.ljust(20, "O")
print(x)

x = txt.rjust(20, "O")
print(x)

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) #hELLO mY nAME iS peter

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)
txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x) #Hello B2B2B2 And 3G3G3G

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
txt = "I could eat bananas all day"

x = txt.partition("bananas")
print(x) #('I could eat ', 'bananas', ' all day')
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x) #('I could eat bananas all day', '', '')

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x) #three three was a race horse, two two was one too.

#last occurance of the string
txt = "Mi casa, su casa."
x = txt.rfind("casa") #12
print(x)
x = txt.rfind("a", 5, 10)
print(x)
print(txt.rfind("q")) #-1
print(txt.rindex("q")) #error

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x) #('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
x = txt.rpartition("apples")
print(x) #('I could eat bananas all day, bananas are my favorite fruit', '', '')

txt = "welcome to the jungle"
x = txt.split()
print(x)
txt = "apple#banana#cherry#orange"
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

#The rsplit() method splits a string into a list, starting from the right.
#If no "max" is specified, this method will return the same as the split() method.
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
# setting the max parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x) #['apple, banana', 'cherry']

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x) #['Thank you for the music', 'Welcome to the jungle']
x = txt.splitlines(True)
print(x) #['Thank you for the music\n', 'Welcome to the jungle']

a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10)) #00000hello
print(b.zfill(10)) #welcome to the jungle
print(c.zfill(10)) #000010.000

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

print('a\
.. b\
... c')
print('foo\\bar')
print('foo\tbar')
print("a\nb")
print('\u2192 \N{leftwards arrow}')
print(r'foo\nbar')
