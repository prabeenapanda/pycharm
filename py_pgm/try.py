#Statements in the except block(s) are executed when an exception is caught. Statements in the
# else block are executed when no exception occurs.
#The try statement in Python can have an optional finally clause.
# This clause is executed no matter what, and is generally used to release external resources.


a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))
    print("Fourth element = %d" % (a[3]))
except IndexError:
    print("An error occurred")


def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


try:
    raise NameError("Hi there")  # Raise Error If we want to modify the builtin arg message                            # we have to use raise like this
except NameError:                 #the arg "hi there" is like parameter which is changed with "an exception"
    print("An exception")
    #raise


#userdefined exception
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.value = arg
try:
    print("hi")
    raise Networkerror("Error ") #as it is given as arg so it take string indexwise
except Networkerror as e:
    print(e.args)  #('E', 'r', 'r', 'o', 'r', ' ')


# class MyError is derived from super class Exception
class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value #as it is given as value it will will that at single value
try:
    raise (MyError(3 * 2))
# Value of Exception is stored in error
except MyError as error: #giving alias name
    print('A New Exception occured: ', error.value)


#Exception is the base class so if i want to use
# any subclass i have to call that after that only i can use the subclass of it in by inheritance
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass
class TransitionError(Error):
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
try:
    raise (TransitionError(2, 3 * 2, "Not Allowed"))
# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occured: ', error.msg)