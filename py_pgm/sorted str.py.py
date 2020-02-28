#Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form
items = input("Enter comma separated words:")
word=[]
for i in items.split(","):
     word.append(i)
print(word)
print(",".join(sorted(word)))
