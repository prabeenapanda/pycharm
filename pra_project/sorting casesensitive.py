l=['a','A','b','B','d','D','c','C']
#l.sort()
print(l)
for i in range(len(l) - 1, 0, -1):
    for j in range(i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)