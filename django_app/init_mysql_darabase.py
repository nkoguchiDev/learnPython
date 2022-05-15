import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    port="3306",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE django_app")
