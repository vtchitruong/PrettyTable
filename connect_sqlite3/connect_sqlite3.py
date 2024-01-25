import sqlite3
from prettytable import from_db_cursor
from pathlib import Path

if __name__ == '__main__':
    # get the current working directory of the script
    database_file = str(Path(__file__).parent) + '\coffee_shop.sqlite3'

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor() # a database cursor object

    sql = '''SELECT customer_id, customer_name, major
    FROM customers
    WHERE major = 'Vaccinologist'
    ORDER BY customer_name
    '''
    cursor.execute(sql)

    table = from_db_cursor(cursor)

    table.align['customer_name'] = 'l' # align left
    table.align['major'] = 'r' # align right
    print(table)