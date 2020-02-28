#alphabate is avilable or not
str=input("enter a string:")
if any(char.isalpha() for char in str):
      print("alphabets available")
else:
     print("no alphabets")