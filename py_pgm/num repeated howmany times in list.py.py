#check which number is repeated in list howmany times
#l=[10,20,10,10,20,30,15]
l = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    l.append(ele)

print(l)
for j in set(l):
    if (l.count(j) > 1):
          print(j,"repeated for:" ,l.count(j),"times")
    elif(l.count(j)==1):
        print(j,"is not repeated")

