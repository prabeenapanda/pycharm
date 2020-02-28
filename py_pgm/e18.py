# Write a Python class to get all possible unique subsets from a set of distinct intege
import itertools
from itertools import combinations, chain
def findsubsets(s, n):
    return list(map(set, itertools.combinations(s, n)))
s = {1, 2, 3}
n = 2

print(findsubsets(s, n))
