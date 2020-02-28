l=[4,56,2,6,792,90,32]
max=l[0]
ma=l[1]
for i in l:
    if i>max:
        max=i
    if (i > ma and i < max):
        ma = i
print("the 2nd maximum value is:",ma)

