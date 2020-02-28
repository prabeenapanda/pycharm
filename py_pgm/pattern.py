f=['a','b','c','d','e','f','g','h','i']
count = 0
for i in f:
    if count == 0:
        print(i.ljust(10,'*'))
        count+=1
    else:
        c=i+"*"*count+i
        print(c.ljust(10,'*'))
       # print(c.ljust(len(f)-count-2,'*'))
        count+=1
