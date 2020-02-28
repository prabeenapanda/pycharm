import mysql.connector


class Connection:
    def __init__(self, host, username, password, database):
        try:
            self.conn = mysql.connector.connect(host=host, user=username, passwd=password, database=database)
            self.connection = self.conn.cursor()

        except mysql.connector.Error:
            print('Database Connection Failed.')
            exit()

