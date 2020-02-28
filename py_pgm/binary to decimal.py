n=int(input("enter the value of n:"))
dec=0
i=1
while n>0:
    rem=n%10
    dec=dec+rem*i
    n=n/10
    i=i*2
print(dec)