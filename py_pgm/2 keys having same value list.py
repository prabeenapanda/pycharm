dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}
print("initial_dictionary", str(dict))
flip = {}

for key, value in dict.items():
    if value not in flip:
        flip[value] = [key]
    else:
        flip[value].append(key)

print("final_dictionary", str(flip))