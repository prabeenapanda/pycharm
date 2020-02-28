n=int(input("enter the value of n:"))
bin=0
i=1
while n>0:
    rem=int(n%2)
    bin=bin+(rem*i)
    n=n/2
    i=i*10
print(int(bin))