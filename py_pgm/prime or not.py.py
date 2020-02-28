#. take a number from the user and check whether it is prime?
no=int(input("enter a number:"))
c=0
if(no>=0):
    for i in range(2,no):
         if no%i==0:
              c=c+1
    print(c)
    if(c==0):
        print("prime number")
    else:
        print("not prime number")
else:
    print("can not check")
