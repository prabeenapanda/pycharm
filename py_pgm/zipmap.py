name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]
mapped = zip(name, roll_no, marks)
print(mapped) #prints the memory location
# converting values to print as list
mapped = list(mapped)
print ("The zipped result is : ",end="")
print (mapped)
print("\n")
# unzipping values
namz, roll_noz, marksz = zip(*mapped)
print ("The unzipped result: \n",end="")
print(namz)#('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')
print ("The name list is : ",end="")
print (list(namz))
print ("The roll_no list is : ",end="")
print (list(roll_noz))
print ("The marks list is : ",end="")
print (list(marksz))

players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]
scores = [100, 15, 17, 28, 43]
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))


l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

