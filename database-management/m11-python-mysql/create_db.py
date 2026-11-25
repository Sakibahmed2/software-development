import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@1qwasz331"
)

db_name = "python_test_db"

mycursor = mydb.cursor()

query = "CREATE DATABASE " + db_name

mycursor.execute(query)
