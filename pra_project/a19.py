#Play a number guessing game (User enters a guess, you print YES or Higher or Lower)
n=int(input("enter a number:"))
x=5
if(x==n):
    print("yes")
elif(n>x):
    print("higher")
else:
    print("lower")