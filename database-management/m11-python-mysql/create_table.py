import mysql.connector

db_name = "python_test_db"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@1qwasz331",
    database=db_name
)


mycursor = mydb.cursor()

query = """
    CREATE TABLE Student( 
        Roll varchar(5),
        Name varchar(100)
    )
""" 

mycursor.execute(query)
