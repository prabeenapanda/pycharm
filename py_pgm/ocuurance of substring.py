#findout nth occurance of given substring
str=input("enter the string:")
sub=input("enter substring:")
occ=int(input("enter the occurance:"))
c=-1
for i in range(0,occ):
     c = str.find(sub, i+1)
print(c)


