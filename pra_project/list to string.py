l=[1,2,3]
li=[]
st=""
for i in l:
    li.append(str(i))
print(li)
for j in li:
    st= st+j
print(st)
#or
s="".join(li)
print(s)