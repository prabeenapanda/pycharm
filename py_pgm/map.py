list_a = [1, 2, 3]
list_b = [10, 20, 30]

q=map(lambda x, y: x + y, list_a, list_b)
print(list(q))
# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
	return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
