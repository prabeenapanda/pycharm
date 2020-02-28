#  program to remove duplicates from dict
dict={1: 'p', 2: 'q', 3: 'r', 4: 's', 5: 't',1:'u'}
dic={}
for key,value in dict.items():
    if key not in dic.keys():
        dic[key]=value

print(dic)
