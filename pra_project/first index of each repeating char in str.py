str=input("enter a string:")
set=set()
for i in str:
    set.add(i)
for j in set:
    print("index of "+j+" is:", str.index(j))
