#List of tuples to dictionary conversion

tup = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(dict(tup))


dict = {'Geeks': 10, 'for': 12, 'Geek': 31}
list = [(k, v) for k, v in dict.items()]
print(list)