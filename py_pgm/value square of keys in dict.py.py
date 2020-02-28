# print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.

d = {}
for x in range(1, 16):
    d[x] = x ** 2
print(d)
#if U want to modify the values u have to do operation on key only here but if u do not want to modify the
#value