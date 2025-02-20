# simple mysql connection python code

import mysql.connector
connection = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "password" , database = "my_db")

if connection.is_connected() == False:  # if no connection made
    print('Erorr : Connection not found')
cur = connection.cursor()   # object for cursor function
cur.execute('select * from stu_id')     # executing sql query
data = cur.fetchall()       # receving response from mysql server into data variable
for i in data:
    print (i)

connection.close()  # close connection & prevent potential memory leaks