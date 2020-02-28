import mysql.connector
import datetime
#CREATE DATABASE "database_name"
db = mysql.connector.connect(user='myuser',
        password='root', host='localhost', port='3376')
#db = mysql.connector.connect(host="localhost", user="root", password="root")
db1 = db.cursor()
db1.execute('CREATE DATABASE test1')
option=input("enter the option:")
if (option=="data"):
     data=int(input("enter the amount of data needed in tb:"))
     date=input("enter the date of purchase:")
     use=int(input("enter the amount of data used in gb:"))
     if use>data:
          print("space exceeded.....")
     else:
          left=data*1000-use
          print("The amount of data left in gb for the user is:%d"  %left)
          cost=use*1000*500
          print("the amount to be paid for the user is:%d" %cost)
mySql_insert_query = """INSERT INTO cloud (Id, Name, Price, Purchase_date)
                           #VALUES (1,tb,tb*1000*1000, '2019-08-14') """
if (option=="date"):
     date=input("enter the date of purchase:")
     year = int(input('Enter a year:'))
     month = int(input('Enter a month:'))
     day = int(input('Enter a day:'))
     first = datetime.date(year, month, day)
     m=int(input("enter for how many months cloud is needed:"))
     last= first + datetime.timedelta(m*365/12)
     print("the maturity date is:" + last.isoformat())
     delta =datetime.date.today() - first
     print("The days left for the user is:%d" %(m*30-delta.days))

