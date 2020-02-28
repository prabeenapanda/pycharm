#a = ['mon','tue','wed','thu','fri','sat']
#now take a integer input from the user and print the day of that number.
a = ['sun','mon','tue','wed','thu','fri','sat']
day=int(input("enter the day:"))
for i,d in enumerate(a):
    if(i==day):
        print(d)


