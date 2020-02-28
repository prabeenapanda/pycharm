def myfun():
    """
        Menu:

1. windows

2. Linux

3. Mac

4. quit

        """
no=int(input("enter the value:"))
if(no==1):
      print("This is windows os")
      print(myfun.__doc__)
elif(no==2):
      print("This is Linux os")
      print(myfun.__doc__)
elif(no==3):
      print("This is Mac Os")
      print(myfun.__doc__)
elif(no==4):
     pass
myfun()