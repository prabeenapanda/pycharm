#take values from console with @ add 5 to all the values replace @ with % and print the sum of all the values.
l=input("enter a string:")
p=l.split('@')
#print(p)
K = 5
res = [int(x) + K for x in p]
#print(res)
s=0
for i in res:
    s=s+i
print(s)
q=map(str,res)
print("%".join(q))

