import functools
import operator
import itertools
lis = [1, 3, 5, 6, 2,0]
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
# using reduce to compute sum of list using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))
# using reduce to compute product using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))
# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))
#diff between accumulate and reduce
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))
