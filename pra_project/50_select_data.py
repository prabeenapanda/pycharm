from db_operations import DB

dbo = DB()
print(dbo.select_table('tbl_emp', conditions=[{"fieldname": "Id", "operator":"=", "value":2}]))
