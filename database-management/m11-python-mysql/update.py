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
    UPDATE student
    SET Name = "Sakib Ahmed Loskor"
    WHERE Roll = "7780"
""" 

mycursor.execute(query)
mydb.commit()