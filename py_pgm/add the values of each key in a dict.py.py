#add the values of each key in a dict
l=[1,2,3]
print(sum(l))
dict1 = { '1.2' : [1, 2, 3] , '2.2' : [4, 5, 6] , '3.3' :[7, 8, 9]}
dict2 = {}
for key in dict1:
    dict2[key] = sum(dict1[key])

print(dict2)