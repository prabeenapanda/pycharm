#delet 2 values at the same time from dictionary.
dic={1:"a",2:"e",3:"t",4:"kl",5:"j"}
di={}
n=input("enter the value:")
m=input("enter another value:")
for key in list(dic.keys()):  ## creates a list of all keys
     if dic[key] == n or dic[key] == m:
            del dic[key]
print(dic)


