Dict = { }
print("Initial nested dictionary:-")
print(Dict)

Dict['Dict1'] = {}

# Adding elements one at a time
Dict['Dict1']['name'] = 'Bob'
Dict['Dict1']['age'] = 21
print("\nAfter adding dictionary Dict1")
print(Dict)

# Adding whole dictionary
Dict['Dict2'] = {'name': 'Cara', 'age': 25}
print("\nAfter adding dictionary Dict1")
print(Dict)
# Prints value corresponding to key 'name' in Dict1
print(Dict['Dict1']['name'])

# Prints value corresponding to key 'age' in Dict2
print(Dict['Dict2']['age'])
 #Deleting dictionary using del keyword
print("\nDeleting Dict2:-")
del Dict['Dict2']['name']
print(Dict)

# Deleting dictionary using pop function
print("\nDeleting Dict1:-")
Dict.pop('Dict1')#op{}
#del Dict['Dict1']#same as pop {}
print(Dict)
#or
#del Dict['Dict1']['name']
#del Dict['Dict2']['age']
#using pop we can not delete specific element it will delete whole dict
