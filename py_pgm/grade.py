mark=int(input("enter the percentage of the student:"))
if(mark>100 or mark<0):
    print("invalid mark")
elif(mark>=90):
    print("o grade")
elif(mark>=80):
    print("E grade")
elif(mark>=70):
    print("A grade")
elif(mark>=60):
    print("B grade")
elif(mark>=50):
    print("C grade")
elif(mark>=35):
    print("D grade")
else:
    print("Failed")
