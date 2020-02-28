
def ov():
   n=int(input("enter a number:"))
   ans= n
   while (n>1):
       if (n % 2 == 0):
           no = n//2
       else:
           no = n*3

       n = no
       #print(n)
   else:
       print("not possible")
   print(ans)

ov ()




#
