#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned
#it will search till end
#it will check special char is available or not only
import re
str=input("enter a string:")
if (re.search('[_\W]',str)):
    print("special chars available")
else:
    print("not available")
