#WAP> 10 -> 000010
       #100 ->  000100
      #1000 ->  001000
  #2345678  ->  2345678
n=input("enter the number:")
c=0
for i in n:
    c=c+1
print(c)
#c=len(n)
m=int(input("enter no of digits:"))
p=m-c
print(p*"0"+n)
print(n.zfill(5))
