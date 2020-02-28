#same as as3
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
d=int(input("enter number 4:"))
if(a==b or a==c or a==d or b==c or b==d or c==d):
    print("error")
else:
    if(a>b) :
        if(a>c):
            if(a>d):
              print("a is largest")
            else:
             print("d is largest")
    elif(b>c):
        if(b>d):
            print("b is largest")
        else:
            print("d is largest")
    elif(c>d):
         print("c is largest")
    else:
         print("d is largest")
