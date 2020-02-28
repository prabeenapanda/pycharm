#give 4 nubers if same no print error else check the greatest
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
d=int(input("enter number 4:"))
if(a==b or a==c or a==d or b==c or b==d or c==d):
    print("error")
else:
    if(a>b and a>c and a>c):
        print("a is largest")

    elif(b>c and b>d):
        print("b is largest")

    elif(c>d):
        print("c is largest")

    else:
        print("d is largest")