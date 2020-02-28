from db_operations import DB

dbo = DB()

dbo.delete_table('tbl_emp', conditions=[{"fieldname": "Id", "operator":"=", "value":2}])

