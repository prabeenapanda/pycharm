def recur(length):
    if(length<=1):
        return length
    else:
        return(recur(length-1)+recur(length-2))
length=int(input("enter the term value:"))
for i in range(length):
    print(recur(i))