#we have use search over here nd $ is not needed as serach will check till end
#cap let available or not
import re
str=input("enter a string:")
if (re.search('[A-Z]',str)):
    print("capital letters available")
else:
    print("not available")