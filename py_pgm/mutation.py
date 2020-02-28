foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']

print(foo)
# Expected Output: ['hi']
# Output: ['hi', 'bye']

print(bar)
# Output: ['hi', 'bye']
def add_to(num, target=[]):
    target.append(num)
    return target
print(add_to(1))
# Output: [1]
print(add_to(2))
# Output: [1, 2]
print(add_to(3))
# Output: [1, 2, 3]
