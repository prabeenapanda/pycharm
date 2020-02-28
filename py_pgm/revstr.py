def reverse(string):
    string = string[::-1]
    return string
s = "Geeks for geeks"
print("The original string  is : ", end="")
print(s)
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))
str = ""
for i in s:
    str = i + str
print(str)
print(s[::-1])


def reverseWords():
    str=input("Enter a sentence:")
    inputWords = str.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output
print(reverseWords())


