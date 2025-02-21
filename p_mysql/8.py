# login verification via mysql table
# pip install bcrypt - to use encription

import bcrypt
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

    hashed_name = bcrypt.hashpw(u_name.encode('utf-8'), bcrypt.gensalt())
    hashed_pwd = bcrypt.hashpw(u_pwd.encode('utf-8'), bcrypt.gensalt())

    cursor = connection.cursor()

    query = "INSERT INTO login (u_name, u_pass) VALUES (%s, %s)"
    cursor.execute(query, (hashed_name, hashed_pwd))
    connection.commit()

    print("User registered successfully")

    connection.close()