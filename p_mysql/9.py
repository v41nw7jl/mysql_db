import mysql.connector
import bcrypt
from getpass import getpass

# Establishing connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="my_db"
)

if not connection.is_connected():
    print('Error: Connection not found')
else:
    def register():
        u_name = input('Enter username: ')
        u_pwd = getpass('Enter password: ')

        # Encrypt the username and password
        hashed_name = bcrypt.hashpw(u_name.encode('utf-8'), bcrypt.gensalt())
        hashed_pwd = bcrypt.hashpw(u_pwd.encode('utf-8'), bcrypt.gensalt())

        cursor = connection.cursor()
        query = "INSERT INTO login (u_name, u_pass) VALUES (%s, %s)"
        cursor.execute(query, (hashed_name, hashed_pwd))
        connection.commit()
        print("User registered successfully")

    def login():
        u_name = input('Enter username: ')
        u_pwd = getpass('Enter password: ')

        hashed_name = bcrypt.hashpw(u_name.encode('utf-8'), bcrypt.gensalt())

        cursor = connection.cursor()
        query = "SELECT u_pass FROM login WHERE u_name = %s"
        cursor.execute(query, (hashed_name,))
        result = cursor.fetchone()

        if result:
            stored_pwd = result[0]
            if bcrypt.checkpw(u_pwd.encode('utf-8'), stored_pwd.encode('utf-8')):
                print("Login successful")
            else:
                print("Login unsuccessful")
        else:
            print("Login unsuccessful")

    print("Press 1 for login")
    print("Press 2 for register")
    choice = input("Enter choice: ")

    if choice == '1':
        login()
    elif choice == '2':
        register()
    else:
        print("Invalid choice")

    connection.close()