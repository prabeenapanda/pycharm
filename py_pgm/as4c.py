#same as as4
dic={'classes':[{'python':[{'nag':['07:00am','02:00pm','04:00pm','10:00pm']},\
        {'siva':['10:00am','05:00pm']}]},{'django':[{'nag':['11:00am','01:00pm']}]}]}
#print(list(dic.keys()))
x = dic["classes"]#to get the value
#print(x)
xx=x[0]
#print(xx)
y=xx['python']
#print(y)
yy=y[0]
#print(yy)
yyy=y[1]
#print(yyy)
d=yyy['siva']
print(d)
t=len(d)
#print(t)
z=yy['nag']
#print(z)
#print(len(z))
p=len(z)
s=t+p
print("total python classes are:",s)
a=x[1]
#print(a)
b=a["django"]
#print(b)
cv=b[0]
#print(cv)
dc=cv["nag"]
#print(dc)
#print(len(d))
r=len(d)
print("total django classes are:",r)
q=p+r
c=0
print("classes nag have are:",q)
substr='am'
c=0
for y in d:
        if substr in y:
             c=c+1
#print(c)
cc=c
for yy in z:
    if substr in yy:
        cc=cc+1
#print(cc)
ccc=cc
for yyy in dc:
    if substr in yyy:
        ccc=ccc+1
print("total no of morning classes are:",ccc)



