n=int(input("enter a number:"))
original=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if(rev==original):
    print("pallindrome")
else:
    print("not pallindrome")