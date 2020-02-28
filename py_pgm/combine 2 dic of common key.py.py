# program to combine two dictionary adding values for common keys.
dic1={"a":1,"b":2,"c":3,"d":4}
dic2={"h":5,"b":6,"c":7,"d":8}
dic3={}
for k in dic1:
    for l in dic2:
        if k==l:
           dic3[k] = dic1[k]+dic2[l]
print(dic3)