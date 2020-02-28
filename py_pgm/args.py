  # Python program to illustrate
# *args with first extra argument
def myFun(ar,arr, *args):
	print ("First argument :", ar)
	for arg in args:
		print("Next argument through *args :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# Python program to illustrate **kargs for
# variable number of keyword arguments with
# one extra argument.

def Fun(arg, **kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
Fun("Hi", first ='Geeks', mid ='for', last='Geeks')


def myF(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myF(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myF(**kwargs)

