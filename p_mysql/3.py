# retriving values from table into python from user.

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
        # Prompt user for table name
        table_name = input("Enter the table name: ")
        
        # Use the user-provided table name in the execute command
        query = f"SELECT * FROM {table_name};"
        c_execute.execute(query)

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