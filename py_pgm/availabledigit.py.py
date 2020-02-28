#pgm to check digit is avilable or not in string
str=input("enter a string:")
if any(char.isdigit() for char in str):
      print("digits available")
else:
     print("no digits")