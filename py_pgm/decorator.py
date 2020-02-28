def smart_divide(func):
   def inner():
      a =int(input("enter the value of a:"))
      b=int(input("enter the value of b:"))
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
      else:
         return func(a,b)
   return inner

@smart_divide
def divide(a,b):
   print("done")
   return a/b
print(divide())


#if you are giving arg in fun def then u should pass the value for the arg in the call otherwise it will show error if u give arg also
#it will show error so if u are getting the value from the console then there is no need of any function call
#but if here u do not give arg we will not be able to return so it is highly needed over here.

# @smart_divide
# def divide():
#    print("done")
# divide()
#we can do it like thish also if there is nothing to return
