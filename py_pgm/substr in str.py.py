#prog to check substring is present in astring or not
str=input("enter a string:")
print(str)
substr=input("enter substring to check:")
print(substr)
x=str.find(substr)
print(x)
if(x==-1):
    print("sub string is not found")
else:
    print("sub string found on position:",x)