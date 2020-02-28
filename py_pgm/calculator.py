class myClass():
   def calculator(self):
       print("welcome")
       a=int(input("enter the value of a:"))
       b=int(input("enter the value of b:"))
       opt=input("enter any operator")
       try:
           if(opt=='+'):
               result=a+b
               print("the result is:",result)
           elif(opt=='-'):
               result=a-b
               print("the result is:",result)
           elif(opt=='*'):
               result=a*b
               print("the result is:",result)
           elif(opt=='/'):
               result=a/b
               print("the result is:",result)
           else:
               print("enter a valid operator")
       except ZeroDivisionError as e:
            print("we should not divide with zero"+ str(e))
       except ValueError:
            print("invalid ")
def main():
   c= myClass ()
   c.calculator()
if __name__ == "__main__":
    main()
