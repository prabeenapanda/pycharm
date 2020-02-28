#check given key already exists in a dictionary.
dic={1:"p",2:"r",3:"q"}
key=input("enter a key:")

if int(key) in dic:
    print("key already exists")
else:
    print("key not available")