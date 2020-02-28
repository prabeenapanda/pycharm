l =[1,1,1,2,2,2,3,3,4,4,4]
max = len(l)
i = 0
while i < max:
    if l[i] != l[i+2]:
        print("Find it at position:",i)
        print("The element is:",l[i])
        break
    i = i + 3