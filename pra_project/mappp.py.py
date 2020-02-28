# map() function is used to apply a function on all the elements of specified iterable and return map object. map object is an iterator,
# map(function, iterables)

def square(x):
    return x**2

result = map(square, range(1, 10))
resultt = map(lambda x:x**2, range(1, 10))
print(list(result))
print(list(resultt))
