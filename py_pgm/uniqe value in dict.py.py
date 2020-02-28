#.print all unique values in a dictionary.
dict={1: 'p', 2: 'q', 3: 'r', 4: 's', 5: 't',6: 's'}
list=[]
for value in dict.values():
    if value not in list:
        list.append(value)
#print(list)
for i in list:
    print(i)