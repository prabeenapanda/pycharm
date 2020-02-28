#find the index of 3rd occurance of 10
a=[10,20,30,10,40,20,50,10,70,80,10,90]
print(a.index(10,4))#this is hardcorded so it will show error sometimes
print(a.index(10,a.index(10,a.index(10)+1)+1))
#for i,val in enumerate(a):
    #print("index is %d and value is %d"%(i,val))
count = 0
n=3
for i,val in enumerate(a):
    if val==10:
        count = count + 1
        if count==n:
            print(i)
            break