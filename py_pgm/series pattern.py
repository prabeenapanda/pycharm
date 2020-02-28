#1,1,2,3,4,9,8,27,16,81,32,.......
n=int(input("enter the number:"))
for i in range(1,n):
    if i%2==1:
        t=(i+1)/2
        res=2**(t-1)
        print(res)
    else:
        t=i/2
        res=3**(t-1)
        print(res)
print()

#10,7,12,9,14,11,16,13
no=int(input("enter a number:"))
term=int(input("enter the term:"))#5
for i in range(1,no):
    if(i%2==1):
        term=term+5
        print(term)
    else:
        term=term-3
        print(term)
print()

#0,0,7,6,14,12,21,18....
m=int(input("enter a number:"))
for i in range(1,m):
    if(i%2==1):
        res=7*((i-1)/2)
        print(res)
    else:
        res=6*((i-2)/2)
        print(res)
print()
