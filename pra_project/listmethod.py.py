# # list out string functions?

upper()	        # Converts a string into upper case
lower()	        # Converts a string into lower case
title()	        # Converts the first character of each word to upper case
capitalize()	# Converts the first character to upper case
casefold()	    # Converts string into lower case
swapcase()	    # Swaps cases, lower case becomes upper case and vice versa

islower()	    # Returns True if all characters in the string are lower case
istitle() 	    # Returns True if the string follows the rules of a title
isupper()	    # Returns True if all characters in the string are upper case

isnumeric()	    # Returns True if all characters in the string are numeric
isalnum()	    # Returns True if all characters in the string are alphanumeric
isalpha()	    # Returns True if all characters in the string are in the alphabet
isdecimal()	    # Returns True if all characters in the string are decimals
isdigit()	    # Returns True if all characters in the string are digits
isidentifier()	# Returns True if the string is an identifier
isprintable()	# Returns True if all characters in the string are printable
isspace()	    # Returns True if all characters in the string are whitespaces

endswith()	    # Returns true if the string ends with the specified value
startswith()	# Returns true if the string starts with the specified value

count()         # Returns the number of times a specified value occurs in a string
encode()	    # Returns an encoded version of the string

expandtabs()	# Sets the tab size of the string

format()	    # Formats specified values in a string
format_map()	# Formats specified values in a string

strip()	        # Returns a trimmed version of the string
lstrip()	    # Returns a left trim version of the string
rstrip()	    # Returns a right trim version of the string

join()	        # Joins the elements of an iterable to the end of the string

center()	    # Returns a centered string
rjust()	        # Returns a right justified version of the string
ljust()	        # Returns a left justified version of the string

partition()	    # Returns a tuple where the string is parted into three parts
rpartition()	# Returns a tuple where the string is parted into three parts

split()	        # Splits the string at the specified separator, and returns a list
rsplit()	    # Splits the string at the specified separator, and returns a list
splitlines()	# Splits the string at line breaks and returns a list

replace()	    # Returns a string where a specified value is replaced with a specified value
find()	        # Searches the string for a specified value and returns the position of where it was found
rfind()	        # Searches the string for a specified value and returns the last position of where it was found
index()	        # Searches the string for a specified value and returns the position of where it was found
rindex()	    # Searches the string for a specified value and returns the last position of where it was found

translate()	    # Returns a translated string
maketrans()	    # Returns a translation table to be used in translations
zfill()	        # Fills the string with a specified number of 0 values at the beginning