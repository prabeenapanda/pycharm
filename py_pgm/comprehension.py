odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)
string = "my phone number is : 11122 !!"
numbers = [x for x in string if x.isdigit()]
print(numbers)
print([x.lower()for x in ["A", "B", "C"]])

a = 5
table = [[a, b, a * b] for b in range(1, 11)]
print("\nMultiplication Table")
for i in table:
    print(i)
    # Python code to demonstrate dictionary
    # creation using dict comprehension
myDict = {p: p ** 2 for p in [1, 2, 3, 4, 5]}
print(myDict)
# Python code to demonstrate dictionary
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)

#set comprehension
set = {x**2 for x in [1, 1, 2]}
print(set)
# Output: {1, 4}

mdict= {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mdict_frequency = {k.lower(): mdict.get(k.lower(), 0) + mdict.get(k.upper(), 0)
                   for k in mdict.keys()}
print(mdict_frequency)
#tuple comprehension is not possible
# generator comprehension don’t allocate memory for the whole list but generate one item at a time,
# thus more memory efficient.
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
  print(x)
  # Outputs numbers

