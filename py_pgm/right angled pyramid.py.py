#.write a program to display #'s in Right angled Triangled form
n=int(input("enter the value of n:"))
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=' ')
    print()
def revert():
    n=int(input("enter the value of n:"))
    for i in range(1,n+1):
        print((n-i)*" "+i*"#")
revert()
    #
   ##
  ###
 ####
#####