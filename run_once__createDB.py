import mysql.connector

mydb= mysql.connector.connect (
    host = "localhost",
    user="root",
    passwd= "TheLevys@Almagor2021",

)

my_cursor= mydb.cursor()

# my_cursor.execute("CREATE DATABASE aitan_roni")

my_cursor.execute ("SHOW DATABASES")

for db in my_cursor:
    print (db)