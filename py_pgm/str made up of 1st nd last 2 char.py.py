#string made of the first 2 and the last 2 chars from a given a string.  If the string length is less than 2,
#return instead of the empty string
def string():
   str=input("enter a string:")
   if len(str) < 2:
        return
   else:
       subs = str[0:2] + str[-2:]
       print("sub string is:"+subs)
string()

