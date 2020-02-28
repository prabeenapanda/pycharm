
str="abc"
l=[]
l.append([])
for i in range(len(str)):
    l.append(list(str[i]))
    l.append(list(str[i:i+2]))
    l.append(list(str[i:i + 3]))
#print(l)
    #l.append(list(str[i:-i]))
list=[]
for i in l:
    if i in list:
        pass
    else:
        list.append(i)
print(list)

