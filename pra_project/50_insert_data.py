from db_operations import DB

dbo = DB()
employee = {'Name': 'Sanjib', 'Dept': 'ADMS'}
dbo.insert_table('tbl_emp', employee)
