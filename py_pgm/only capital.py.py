# $ is used to check till end we can not skip $
#match only check in the begning
#it checks all the letters whether anything else available or not otherthen that also it checks that
#take a string from the user and check contains only  capital letters or not?
import re
str=input("enter a string:")
if not re.match('[A-Z]+$', str):
    print("not only capital letters")
else:
    print("only capital letters")

#if char.isupper==true