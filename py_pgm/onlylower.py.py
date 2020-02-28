#here it can be done using only match not search
# $ is used to search till end
#take a string from the user and check contains only  small letters or not
str=input("enter a string:")
if not re.match('[a-z]+$', str):
    print("not only small letters")
else:
    print("only small letters")