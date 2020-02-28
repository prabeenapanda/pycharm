#small let available or not
import re
str=input("enter a string:")
if (re.search('[a-z]',str)):
    print("small letters available")
else:
    print("not available")