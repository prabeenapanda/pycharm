#print uniq elements of the list as keys of dict
mylist = ["a", "b", "a", "c", "c"]
list = list(dict.fromkeys(mylist))
print(list)