#l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
#output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
l=[1,1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
parent_array = []
arr=[]
for i in range(len(l)-1):
    # print(i)
    # print(l[i])
    if l[i] == l[i+1]:
        arr.append(i)
    else:
         arr=[]
parent_array.append(arr)
print(parent_array)

