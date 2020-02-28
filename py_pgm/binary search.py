a=[1,2,3,4,5,6,7,87,90]
b=0
e=len(a)-1
item=int(input("enter item to be checked:"))
m=int((b+e)/2)
print(a[m])
while(b<e and item!=a[m]):
    if(item<a[m]):
        e=m-1
    else:
        b=m+1
    m=int((b+e)/2)
if(item==a[m]):
    print("item found at "+str(m)+" position")
else:
    print("item not found")