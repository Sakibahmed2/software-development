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
    INSERT INTO Student(Roll, Name) VALUES("7780", "Sakib Loskor")
""" 

mycursor.execute(query)
mydb.commit()