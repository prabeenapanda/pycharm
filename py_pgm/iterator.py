# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
## iterate through it using next()

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
print(next(my_iter))
#An object is called iterable if we can get an iterator from it.
# Most of built-in containers in Python like: list, tuple, string etc. are iterables.
#iterator gives memory efficiancy if we range (o,10) it will take 1 memory address at a time then will delete
#previous value and again i new memory to give value.but normally for loop will take 10 memory at time
