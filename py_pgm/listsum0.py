lis=[]
n=int(input("enter a no:"))
for i in range(-2,3):
    lis.append(i)
print(lis)
if len(lis)>n:
    raise exception("error")
print(sum(lis))
