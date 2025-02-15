# inserting values into table and printing updated table.

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
        c_execute = mydb.cursor()  # Create a cursor object to execute SQL queries

        # Prompt user for input
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        major = input("Enter the student's major: ")

        # Insert the user-provided data into the Students table
        query = "INSERT INTO Students (Name, Age, Major) VALUES (%s, %s, %s)"
        values = (name, age, major)
        c_execute.execute(query, values)
        mydb.commit()  # Commit the transaction

        print("Record inserted successfully!")

        # Printing updated table.
        query = f"SELECT * FROM Students;"
        c_execute.execute(query)

        tables = c_execute.fetchall()        
        print("Updated List :")
        for table in tables:
            print(table)

except sq.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if mydb and mydb.is_connected():
        c_execute.close()  # Close the cursor
        mydb.close()  # Close the connection
        print("MySQL connection is closed")