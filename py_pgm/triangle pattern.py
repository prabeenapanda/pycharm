#reverted  triangle
n=int(input("enter value of n:"))
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * ' *')
#reverted triangle
def triangle():
    n = int(input("enter value of n:"))
    for i in range(n, 0, -1):
        for j in range(i,n):
            print(end=" ")
        for k in range(0,i):
            print("#",end=" ")
        print()
triangle()