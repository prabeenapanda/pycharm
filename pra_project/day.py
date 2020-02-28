#Write a Python program to add three days in current date and give weekday

from datetime import date, timedelta
dt = date.today() + timedelta(7)
print('Current Date :',date.today())
print('3 days after Current Date :',dt)
print(dt.strftime("%a"))



