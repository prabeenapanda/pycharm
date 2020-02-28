#get a single string from 2 given strings separeted by space and swap the 1st 2 char of both
st1=input("enter first string:")
st2=input("enter the second string:")
a = st2[:2] + st1[2:]
b = st1[:2] + st2[2:]
print(a+' '+b)