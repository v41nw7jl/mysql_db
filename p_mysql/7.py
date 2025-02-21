# login verification via mysql table

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="my_db"
)

if not connection.is_connected():
    print('Error: Connection not found')
else:
    u_name = input('Enter username: ')
    u_pwd = input('Enter password: ')

    cursor = connection.cursor()
    query = "SELECT * FROM login WHERE u_name = %s AND u_pass = %s"
    cursor.execute(query, (u_name, u_pwd))
    #cursor.execute("SELECT * FROM login WHERE u_name = %s AND u_pass = %s", (u_name, u_pwd))

    result = cursor.fetchone()
    if result is not None:
        print("login successful")
    else:
        print("login details incorrect, login un-successful")

    connection.close()