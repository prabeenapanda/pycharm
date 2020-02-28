# calculator
def calculator():
    print("welcome")
    a = int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    opt = input("enter any operator")
    if (opt == '+'):
        try:
            result = a + b
            print("the result is:", result)
        except valueError:
            print("entered value is not valid")
    elif (opt == '-'):
        try:
            result = a - b
            print("the result is:", result)
        except valueError:
            print("entered value is not valid")
    elif (opt == '*'):
        try:
            result = a * b
            print("the result is:", result)
        except zeromultiplicationError:
            print("we should not multipy with zero")
    elif (opt == '/'):
        try:
            result = a / b
            print("the result is:",result)
        except zerodivisionError:
            print("we should not divide with zero")
    else:
        print("invalid operator")

calculator()