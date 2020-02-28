#The is checks if both the variables point to the same object or same memory location
#whereas the == sign checks if the values for the two variables are the same.
#for mutable for same value the size will be different only so 'is' operator will always show false
# but for immutable after some certain memory size the 'is' operator will show false
#the output in ide and cmd is different
import sys
a = b = [1,2,3]
c = [1,2,3]
print(sys.getsizeof(a))#to know the memory size
print(a == b)
#True
print(a == c)
#True
print(a is b)
#True
print(a is c)
#False
list1 = []
list2 = []
list3 = list1
if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")
if (list1 is list3):
    print("True")
else:
    print("False")


a =c= 20
b = 20
print(a == b)#True
print(a is b)#true
print(c==b)#true
print(c is b)#true
print(a==c)#true
print(a is c)#true