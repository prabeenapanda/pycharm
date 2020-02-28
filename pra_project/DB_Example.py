import pymysql
dbcon = pymysql.connect(host = 'localhost', user = 'root', db = 'example', passwd = 'prabeena',)
print(dbcon)