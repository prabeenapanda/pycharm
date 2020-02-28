
lis = [1, 2, 3, 4, 5, 7, 6, 8, 9, 0, 2, 7, 9, 3, 2, 3, 4, 5]
for i in range(len(lis) - 1, 0, -1):
    for j in range(i):
        if lis[j] > lis[j + 1]:
            lis[j], lis[j + 1] = lis[j + 1], lis[j]
print(lis)
max=len(lis)-1
i=0
while(i < max):
    c=1
    while lis[i]==lis[i+1]:
        i += 1
        c += 1
        if i + 1 == len(lis):
            break
    print("the occurance of ",lis[i],"is",c)
    i += 1
print()