# string made of 4 copies of the last two characters of a specified string (length must be at least 2).
str=input("enter a string:")
if len(str)<2:
    print("invalid")
else:
    sub=str[-2:]
    print(sub*4)

