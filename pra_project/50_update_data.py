from db_operations import DB

dbo = DB()

employee_data = {'Name': 'Sanjib Kumar', 'Dept': 'App Development'}
dbo.update_table('tbl_emp',employee_data,
                 [{'fieldname': 'Id', 'operator': '=', 'value': 2, 'conj_operator': ''}])


