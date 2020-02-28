#write a program to check given substring is there in actual string or not?
# (search should be case insensitive)
str=input("enter a string:")
print(str)
substr=input("enter substring to check:")
print(substr)
#subs=substr.casefold()
#print(subs)
#st=str.casefold()
#print(st)
if substr.casefold() in str.casefold():
    print("sub string is found")
else:
    print("sub string is not found")
