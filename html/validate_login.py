import mysql.connector
import cgi
import cgitb
cgitb.enable()

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="my_db"
    )

# Validate login details
def validate_login(username, password):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM login WHERE u_name = %s AND u_pass = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Main function
def main():
    form = cgi.FieldStorage()
    username = form.getvalue('u_name')
    password = form.getvalue('u_pass')
    
    if validate_login(username, password):
        print("Content-type:text/html\r\n\r\n")
        print("<html><body>")
        print("<h2>Login Successful!</h2>")
        print("<meta http-equiv='refresh' content='2;url=home.html' />")
        print("</body></html>")
    else:
        print("Content-type:text/html\r\n\r\n")
        print("<html><body>")
        print("<h2>Invalid Credentials</h2>")
        print("<a href='login.html'>Try Again</a>")
        print("</body></html>")

if __name__ == "__main__":
    main()