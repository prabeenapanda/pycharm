#WAP to find union and intersection of lists
l=[1,2,3,4]
li=[3,4,5,6]
list=(l+li)
lis=li+l

for i in list:
    if list.count(i)==1:
        pass
    else:
        list.remove(i)
print(list)
listt=[]
for i in lis:
    if lis.count(i)>1:
        listt.append(i)
    else:
        pass
s=set(listt)
ll=[]
for i in s:
    ll.append(i)
print(ll)



