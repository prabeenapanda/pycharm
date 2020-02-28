# Python code to demonstrate
# working of next()

# initializing list
list1 = [1, 2, 3, 4, 5]

# converting list to iterator it is must u have to make the list iterator
list1 = iter(list1)

print ("The contents of list are : ")

# printing using next()
# using default
while (1) :
	val = next(list1,'end')
	if val == 'end':
		print ('list end')
		break
	else :
		print (val)
