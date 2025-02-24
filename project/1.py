# Student Database - insert , view

import mysql.connector          # Establish a connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="my_db"
)
cursor = db.cursor()        # Create a global cursor object

def create_table():    
    t_name = input("Enter the name of the table : ")
    n_fields = int(input("Enter the number of fields (max 3) : "))
    
    while n_fields > 3:     # if number of field is more than 3 then ask user to re-enter.
        print("Number of fields cannot exceed 3. Please try again.")
        n_fields = int(input("Enter the number of fields (max 3) : "))

    fields = []     # list to store the name of fields

    for i in range(n_fields):       # using loop to enter details of field.
        field_name = input(f"Enter the name of field {i+1}: ")
        print('Only use either of Data Type : INT, VARCHAR(255)')
        data_type = input(f"Enter the data type of field {i+1} : ")
        fields.append((field_name, data_type))

    # creating a sql query using loop and storing value into a variable for execution.
    create_table_sql = f"CREATE TABLE {t_name} ("
    for i, (field_name, data_type) in enumerate(fields):
        create_table_sql += f"{field_name} {data_type}"
        if i < len(fields) - 1:
            create_table_sql += ", "
    create_table_sql += ")"
    #print(create_table_sql)        # to check query
    
    cursor.execute(create_table_sql)
    db.commit()
    
    print(f"Table : {t_name} , created successfully!")
    input("Press Enter to continue...\n")     # asking user i/p to move to main menu

def insert_values():
    print('Insert Values')

def view_details():
    print('View Details')

def list_tables():
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("List of tables in the database :")
    for i, table in enumerate(tables, start=1):
        print(f"{i}. {table[0]}")
    input("Press Enter to continue...\n")     # asking user i/p to move to main menu

print('Student Database')

while True:
    print("\nMenu:")
    print("1. Create Table")
    print("2. Insert Values")
    print("3. View Details")
    print("4. List Tables")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_table()
    elif choice == "2":
        insert_values()
    elif choice == "3":
        view_details()
    elif choice == "4":
        list_tables()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
