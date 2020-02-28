n=int(input("enter a number:"))
m=int(input("enter another number:"))
if n<m:
    b=n
else:
    b=m
for i in range(1,b):
    if (n%i ==0 and m%i ==0):
         print(i)