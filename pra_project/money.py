mon=[0.50,0.75,0.25,1,5,10]
amt=int(input("enter the amount:"))
min = 100
minn = 50
for i in mon:
    if i==amt:
        print("here is your amount:",amt)
    elif i < amt:
        x=amt//i
        if x < min:
            min=x
print(min,i)
val=i
if amt > min*val:
    dif=amt-(min*i)
    for i in mon:
        if i == dif :
            print("here is ur extra amt:",dif)
        else:
            if i < dif:
               diff=dif-i
               y = diff // i
               if y < minn:
                   minn = y

            elif i > dif:
                diff=i-dif
                z=diff//dif
                if z < minn:
                    minn = z

            print(minn,i)


