import copy
l1=[[1,2,3],5,7]
#l2=copy.deepcopy(l1)
print(l1)
li1 = [1, 2, [3, 5], 4]

# using copy for shallow copy
li2 = copy.copy(li1)
print(li2)
# using deepcopy for deepcopy
#li3 = copy.deepcopy(li1)
#print(li3)
li1[2][0] = 7
print(li2)#change will be reflected
#print(li3) #as it is deepcopy change will not be reflected