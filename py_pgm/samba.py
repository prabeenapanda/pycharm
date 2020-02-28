d={1:'a',2:'b',3:'a'}
di={}
for k,v in d.items():
    if v not in di:
        di[v]=[k]#directly store that keys in list
    else:
        di[v].append(k)#bcoz now it value is the key of d

print(di)