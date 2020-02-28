l=['a','b','c','d','e','f','g','h','i','j']
count = 0
for i in l:
    if count == 0:
       print(''.join(str(x)for x in l))
       count += 1
    else:
        c = i + "*" *(count-1)+ i
        print(c.ljust(10, '*'))
        count += 1

