# retriving data from mysql table into python

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
        # Add command to check the list of tables
        c_execute.execute("SHOW TABLES;")
        tables = c_execute.fetchall()
        print("List of tables in the database:")
        for table in tables:
            print(table)

except sq.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if mydb and mydb.is_connected():
        c_execute.close() # Close the cursor
        mydb.close()     # Close the connection
        print("MySQL connection is closed")