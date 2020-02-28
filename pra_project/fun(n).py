l=[]
def fun(n):
    for i in range(1,n):
        l.append(i)
    for i in range(n-2,0,-1):
        l.append(i)
    return(l)
print(fun(5))
