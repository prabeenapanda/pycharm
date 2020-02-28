import re
str=input("enter a string:")
print(str)
#removes symboles
#sub()
num = re.sub(r'\W', "", str)
print("Phone Num : ", num)
# Remove anything other than digits
num = re.sub(r'\D', "", str)
print("Phone Num : ", num)
#removes anything other than symbols
num = re.sub(r'\w', "", str)
print("Phone Num : ", num)
#removes digits
num = re.sub(r'\d', "", str)
print("Phone Num : ", num)
#removes spaces
num = re.sub(r'\s', "", str)
print("Phone Num : ", num)
#removes anything other than spaces
num = re.sub(r'\S', "", str)
print("Phone Num : ", num)
#removes capital letters
num = re.sub(r'[A-Z]', "", str)
print("Phone Num : ", num)
#removes anything other than Capital letters
num = re.sub(r'[^A-Z]', "", str)
print("Phone Num : ", num)
#Replace the first two occurrences of a white-space character with the digit 9:
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)

#group()
line = "Cats are smarter than dogs" #before 'are' there will be one group and after another
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())#Spain

#findall()
#it checks all the occurance of the pattern
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)#list of 2 ai

#split()
#it split according to given char and returns list
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
#Split the string only at the first occurrence
y = re.split("\s", str, 1)
print(y)

#span()
#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S"
x = re.search(r"\bS\w+", str)
print(x.span())

#Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", str)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", str)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", str)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", str)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#Check if the string starts with "The"
x = re.findall("\AThe", str)
if (x):
  print("Yes, there is a match!")
else:
  print("No match")
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", str)
if (x):
  print("Yes, there is a match!")
else:
  print("No match")

#......METACHAR......
strr = "hello world." \
       "hi hello all bye"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o"
#Matches any single character except newline.
x = re.findall("he..o", strr)
print(x)
##Find all lower case characters alphabetically between "a" and "m".
x = re.findall("[a-m]", strr)
print(x)
#Check if the string starts with 'hello':
x = re.findall("^hello", strr)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
#Check if the string ends with 'world':
x = re.findall("world$", strr)
if (x):
  print("Yes, the string ends with 'bye'")
else:
  print("No match")
#Check if the string contains "a" followed by exactly two "l" characters
x = re.findall("al{2}", strr)
#x = re.findall("al{2,}", strr)  this will check 2 or more occurance
#x = re.findall("al{2,5}", strr)  this will check atleast 2 and at most 5 occurance
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
# Check if the string contains either "all" or "any":
x = re.findall("all|any", strr)
if (x):
     print("Yes, there is at least one match!")
else:
    print("No match")
#Check if the string contains "ai" followed by 0 or more "x" characters
# If there is no such thing also it will be true
x = re.findall("aix*", strr)
print(x)
if (x):
  print("Yes, there is match!")
else:
  print("No match")
#Check if the string contains "ai" followed by 1 or more "x" characters:
#if there is no such thing it will return false
x = re.findall("aix+", strr)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
st = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", st)
if (x):
  print("Yes, there is match!")
else:
  print("No match")
#start()
s = "The rain in Spain"
x = re.search("\s", s)
print("The first white-space character is located in position:", x.start())
#Return an iterator yielding MatchObject instances over all non-overlapping matches for the RE pattern instring.
# The string is scanned left-to-right,and matches are returned in the order found. Empty matches are included in the result.
s1 = 'Blue Berries'
pattern = 'Blue Berries'
for match in re.finditer(pattern, s1):
    s = match.start()
    e = match.end()
    print ('String match "%s" at %d:%d' % (s1[s:e], s, e))