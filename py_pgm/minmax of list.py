import functools
l=[5,2,8,4,1]
print(functools.reduce(lambda a, b: a if a > b else b, l))


max=l[0]
for i in l:
    if i>max:
        max=i
print(max)

min=l[4]
for i in l:
    if i<min:
        min=i
print(min)

