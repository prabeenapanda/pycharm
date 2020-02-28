#1. print count of character’s in string
str=input("enter a string:")
frq={}
for i in str.lower():
    if i in frq:
        frq[i]=frq[i]+1
    else:
        frq[i]=1

print(frq)
