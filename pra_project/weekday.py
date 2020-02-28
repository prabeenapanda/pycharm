def testcode():
    try:
        day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        print(day)
        string = input("Enter a day from the list: ")
        num = int(input("Enter a number between 1 to 7: "))
        sum = 0
        for i in day:
            if i==string:
                sum = day.index(i)
        sum += num
        if sum >=(len(day)-1):
            sum =(sum - (len(day)-1))-1
        print("Day is: ",day[sum])
    except IndexError:
        print("Updating")
testcode()

from itertools import cycle

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pool = cycle(day)
string = input("Enter a day from the list: ")
num = int(input("Enter a number between 1 to 7: "))
sum = 0

for item in pool:
    if item==string:
        sum=day.index(item)
    sum += num
print("Day is: ", day[sum])
