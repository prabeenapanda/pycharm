dic={ 'apple': 5, 'pear': 7 ,'strawberry': 2}
dicc={ 'mango': 5, 'pear': 5,'strawberry': 1}
dd={}
l=[]
ll=[]
lll=[]
for i in dic.keys():
    l.append(i)
for i in dicc.keys():
    ll.append(i)
dd.update(dic)
dd.update(dicc)
print(dd)
for k in dd.keys():
    lll.append(k)
for i in l:
    for j in ll:
        if i==j:
            for k in lll:
                if k==j:
                   dd[k]=dic[i]+dicc[j]
print(dd)




