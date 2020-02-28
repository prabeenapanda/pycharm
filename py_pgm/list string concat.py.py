#1 2 3
#12@11@13
# 13#13#16(output)
l1=input("enter 1st input:")
l2=input("enter 2nd input:")
p=l1.split(' ')
r=l2.split('@')
n=len(p)
q=[]
for i in range(0, n):
        q.append(str(int(p[i])+int(r[i])))

print("#".join(q))

#another way using map and zip
pp=map(int,p)
rr=map(int,r)
qq=[x+y for x,y in zip(pp,rr)]
qqq=map(str,qq)
print("#".join(qqq))
