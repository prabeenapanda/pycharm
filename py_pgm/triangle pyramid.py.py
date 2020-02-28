#Write a program to display #'s in pyramid style
size = int(input("enter the size:"))
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("#", end=' ')
    print(" ")
def pyramid():
    n=int(input("enter the size:"))
    for i in range(1,n+1):
        print((n-i)*" ",i*" *")
pyramid()

