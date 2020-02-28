# The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed,
# and returns an iterator of tuples.
# zip(*iterables)

l1 = [1,2]
l2 = [3,4]
result = [x+y for x, y in zip(l1, l2)]
print(result)

