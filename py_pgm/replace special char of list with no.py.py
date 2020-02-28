#replace the special chars of list with a specific value
a=[1,2,3,"@",4,"$",7,8]
l=["@","$"]
for j in l:
    if j in a:
          a.insert(a.index(j),50)
          a.remove(j)
print(a)
