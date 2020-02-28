#Input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [['1/1-4'], ['2/5-6'], ['2/8']]
input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"]
list=[]
newList=[]
li=[]
ll=[]
lii=[]
new=[]
lll=[]
se=set()
s=set()
for i in input:
    if  i.startswith("1"):
        list.append(i)
print(list)
for i in list:
    newList.append(i.split("/"))
print(newList)
for i in newList:
    for j in i:
        li.append(int(j))
print(li)
for i in li:
    se.add(i)
print(se)
for i in se:
    ll.append(i)
print(ll)
maximum = max(ll)
if sum(ll) == maximum * (maximum+1) /2 :
             print("t")
lis=[]
for i in input:
    if  i.startswith("2"):
        lis.append(i)
print(lis)
for i in lis:
    new.append(i.split("/"))
print(new)
for i in new:
    for j in i:
        lii.append(int(j))
print(lii)
for i in lii:
    s.add(i)
for i in s:
    lll.append(i)
print(lll)
lll.remove(2)
print(lll)
maximum = max(lll)
if sum(lll) == maximum * (maximum+1) /2 :
             print("t")
else:
    print("f")





