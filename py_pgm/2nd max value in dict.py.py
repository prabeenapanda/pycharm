# Python program to find second maximum value in Dictionary.
dict = {"google": 12, "amazon": 9, "flipkart": 4, "gfg": 13}
max = max(dict.values())
max2 = 0
for v in dict.values():
    if (v > max2 and v < max):
        max2 = v
print(max2)
print(list(sorted(dict.values()))[-2])