# **kwargs in function definitions in python is used to pass a keyworded, variable no of argument list.
# args can be accessed as a dictionry inside the function

def get_sql(table, **kwargs):
    sql = f"select * from {table}"
    if 'orderby' in kwargs:
        sql = f"{sql} order by {kwargs['orderby']}"
    if 'limit' in kwargs:
        sql  =  f"{sql} limit={kwargs['limit']}"
    return sql

print(get_sql('users', limit = 10, orderby='id'))
print(get_sql('users', limit = 10))
print(get_sql('users', orderby='id'))
print(get_sql('users'))
