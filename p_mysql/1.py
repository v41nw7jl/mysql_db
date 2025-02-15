# creating connection to mysql from python

import mysql.connector as sq

mydb = None  # Initialize outside try block for wider scope

try:
    mydb = sq.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="my_db"
    )

    if mydb.is_connected():
        c_execute = mydb.cursor()  # Create a cursor object to execute Sql queries
        c_execute.execute("SELECT DATABASE();")
        record = c_execute.fetchone()
        print("You are connected to database: ", record)

except sq.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if mydb and mydb.is_connected():
        c_execute.close() # Close the cursor
        mydb.close()     # Close the connection
        print("MySQL connection is closed")