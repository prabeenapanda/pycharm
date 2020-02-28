#first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
# replace the whole 'not'...'poor' substring with 'good'
str=input("enter a string:")
n=str.find("not")
print(n)
p=str.find("poor")
if n>p:
    str1=str.replace(str[p:(n+3)],"good")
    print(str1)
else:
    print(str)