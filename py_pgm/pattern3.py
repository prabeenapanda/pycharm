def pattern(n):
 num=97
 for i in range(0,n):
     char=chr(num)
     print(char.ljust(10,'*'))
     num=num+1
print(pattern(10))