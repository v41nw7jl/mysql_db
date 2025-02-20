# fetchone() with while loop 

import mysql.connector
connection = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "password" , database = "my_db")

if connection.is_connected() == False:  # if no connection made
    print('Erorr : Connection not found')
cur = connection.cursor()   # object for cursor function
cur.execute('select * from stu_id')     # executing sql query

data = cur.fetchone()       # receving response from mysql server into data variable

while data is not None:
        print(data)
        data = cur.fetchone()

connection.close()  # close connection & prevent potential memory leaks