#as1
from collections import Counter
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(lst)
print(Counter(lst))

