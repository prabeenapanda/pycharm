#Take two numbers from the user a,b check whether a is divisible by b or not?
a=int(input("enter number a:"))
b=int(input("enter number b:"))
try:
    r=a/b
    print("result is:",r)

except ZeroDivisionError:
    print("we should not divide with zero")
except ValueError:
    print("invalid ")
