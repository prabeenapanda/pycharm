import mysql.connector
from db_connection import Connection
from config import DB_config

class DB(Connection):
    host = 'localhost'
    username = 'root'
    password = ''
    database = 'mydatabse'
    def __init__(self):
        Connection.__init__(self, host=DB_config['host'],
                                  username=DB_config['username'],
                                  password=DB_config['password'],
                                  database=DB_config['database'])
        self.sql = ''
        self.fields = ''
        self.table = ''
        self.where_condition = ''
        self.placeholders = []
        self.limit = ''
        self.orderby = ''


    def select(self, fields):
        if fields == '*':
            self.fields = '*'
        else:
            self.fields = ', '.join(fields)

    def where(self, condition):
        # print(condition)
        if len(self.where_condition) == 0:
            self.where_condition = ' where '
        if 'conj_operator' in condition.keys():
            if condition['conj_operator'] == 'and':
                self.where_condition += 'and'
            elif condition['conj_operator'] == 'or':
                self.where_condition += 'or'

        self.where_condition = f"{self.where_condition}  {condition['fieldname']}  {condition['operator']}  %s "
        self.placeholders.append(condition['value'])

    def limit(self, limit: int, offset: int = 0):
        self.limit = f' limit {limit}, {offset} '

    def order_by(self, orderby):
        self.orderby = f' order by {orderby} '

    def select_table(self, table_name, columns='*', conditions=[]):
        self.select(columns)
        for condition in conditions:
            self.where(condition)
        self.sql = f'select {self.fields} from {table_name} {self.where_condition} {self.orderby} {self.limit}'

        try:
            self.connection.execute(self.sql, self.placeholders)
            return self.connection.fetchall()
        except mysql.connection.Error as err:
            print(err)
            return False

    def insert_table(self, table_name, data):
        """
        jjojoi

        iuiuuu
        """
        if len(data) > 0:
            fields = []
            for key in data:
                fields.append(key)
                self.placeholders.append(data[key])
            self.sql = f'INSERT INTO {table_name}  ({",".join(fields)}) values ({",".join([" %s"] * len(fields))})'
            try:
                self.connection.execute(self.sql, tuple(self.placeholders))
                self.conn.commit()
                return True
            except mysql.connector.Error as err:
                print(err)
                return False

    def update_table(self, table_name, data, conditions):
        if len(data) > 0:
            fields = []
            for key in data:
                fields.append(key+" = %s ")
                self.placeholders.append(data[key])
            for condition in conditions:
                self.where(condition)

            self.sql = f'UPDATE {table_name}  SET {",".join(fields)} {self.where_condition}'

            try:
                self.connection.execute(self.sql, tuple(self.placeholders))
                self.conn.commit()
                return True
            except mysql.connection.Error as err:
                print(err)
                return False

    def delete_table(self, table_name, conditions):
        if len(conditions) > 0:
            for condition in conditions:
                self.where(condition)
            self.sql = f'DELETE FROM {table_name}  {self.where_condition}'

            try:
                self.connection.execute(self.sql, tuple(self.placeholders))
                self.conn.commit()
                return True
            except mysql.connection.Error as err:
                print(err)
                return False

    def __create_column(self, column):
        keys = column.keys()
        col_str = column['col_name'] + " " + column['data_type']
        col_str += ' NULL ' if ('null_type' in keys) and column['null_type'] else ' NOT NULL '
        if ('auto_increament' in keys) and column['auto_increament']:
            col_str += " AUTO_INCREMENT "
        if ('primary_key' in keys) and column['primary_key']:
            col_str += " PRIMARY KEY "
        if ('default' in keys) and column['default']:
            col_str += " default = '" + column['default'] + "'"
        return col_str

    def create_table(self, table_name, columns):
        table_columns = []
        for column in columns:
            table_columns.append(self.__create_column(column))
        self.sql = f'create table {table_name} ({", ".join(table_columns)})'

        self.connection.execute(self.sql)
