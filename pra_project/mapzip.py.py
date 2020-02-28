l1 = [1,2]
l2 = [3,4]

result = [x+y for x, y in zip(l1, l2)]
print(result)

result = list(map(lambda x, y: x+y, l1, l2))
print(result)