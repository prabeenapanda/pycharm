from itertools import cycle

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pool = cycle(day)
string = input("Enter a day from the list: ")
num = int(input("Enter a number : "))
sum = 0
for item in day:
    if item==string:
        sum=day.index(item)
sum += num
for i,item in enumerate(pool):
    if i==sum:
       print(item)

