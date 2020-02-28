n=int(input("enter the lower limit:"))
m=int(input("enter the upper limit:"))
for i in range(n,m):
    c = 0
    for j in range(2,i):
        if(i%j==0):
            c=c+1
    #print(c)
    if(c==0):
        print(i)
    else:
        pass

