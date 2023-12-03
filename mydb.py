import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursorObject = dataBase.cursor()
cursorObject.execute('CREATE DATABASE g_stock_py')
print('All done!')