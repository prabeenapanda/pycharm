# Python3 code to demonstrate the
# working of set() on dictionary

# initializing list
dic1 = { 4 : 'geeks', 1 : 'for', 3 : 'geeks' }

# Printing dictionary before conversion
# internaly sorted
print("Dictionary before conversion is : " + str(dic1))

# Dictionary after conversion are
# notice lost keys
print("Dictionary afer conversion is : " + str(set(dic1)))
# Python3 code to demonstrate the
# working of set() on list and tuple

# initializing list
lis1 = [ 3, 4, 1, 4, 5 ]

# initializing tuple
tup1 = (3, 4, 1, 4, 5)

# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
print("The tuple before conversion is : " + str(tup1))

# Iterables after conversion are
# notice distinct and sorted elements
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))
