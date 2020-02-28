#in a txt file write 1st lines already there
#1 2 3 4
#10 11 12 13
#11 13 14 17
f1=open("file1.txt",'r+')
l1=f1.readline()
l2=f1.readline()
p=l1.strip('\n')
q=l2.strip('\n')
pp=p.split(" ")
#print(pp)
qq=q.split(" ")
#print(qq)
n=len(pp)
r=[]
for i in range(0, n):
        r.append(str(int(pp[i])+int(qq[i])))

#print(r)
s=" ".join(r)
#print(s)
f2=open("file1.txt",'a+')
f2.write(s)