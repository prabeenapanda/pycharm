#get a string from a given string where all occurrences of its first char have been changed to '$',
#except the first char itself.
str=input("enter a string:")
ch=str[0]
print(ch)
subs=str[1:].replace(ch,"$")
print(ch+subs)