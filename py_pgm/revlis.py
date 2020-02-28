#l = [1, 4, 6, 8, 90, 3, 2, 5]
s=0
x,y,z=input("enter 3 numbers:").split()#values separeted by space will work but not enter
ss=int(x)+int(y)+int(z)
print("sum of %s,%s,%s is:"%(x,y,z),ss)
r=input("enter numbers:").split(',')
for i in r:
    s=s+int(i)
print(s)
print(r)
ll = []
a= [int(x) for x in input("enter numbers:").split(',')]
ll = []
print(a)
for i in a:
    ll.append(i)
print(ll)
print(ll[::-1])
#if the value u entered is float it can not be converted in to int dirctely
#print(int(float(q)))  {wrong}
# u have to follow below method
q=input("enter a number:")
qq=float(q)
print(qq)
qqq=int(qq)
print(qqq)
