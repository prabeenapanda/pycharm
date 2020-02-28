# *args in function definitions in python is used to pass a variable number of arguments to a function.
# args can be accessed as a list inside the function

def add(a, *args):
    s = a
    for x in args:
        s += x
    return s

print(add (1,2))
print(add(1, 2, 3, 5))



