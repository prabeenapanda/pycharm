#it can only be done using match not search
# take a string from the user and check contains only  special chars or not?
import re
str=input("enter a string:")
if not re.match('[_\W]+$', str):
    print("not only special chars")
else:
    print("only Special chars")

