#indian number
import re
str=input("enter a string:")
print(str)
num = re.sub(r'\D', "", str)
print("Phone Num : ", num)
Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
if(Pattern.match(num)):
    print("valid")
else:
    print("invalid")




