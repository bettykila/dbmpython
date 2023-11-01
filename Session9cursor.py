#import _mysql_connector
import mysql.connector

#create connection
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "ceit")

#create the cursor object
mycursor = conn.cursor()

#mycursor.execute('CREATE DATABASE liklikbukLibrary')
mycursor.execute('USE liklikbukLibrary')

#create table
tablebooks = """CREATE TABLE Books (BookID int primary key, Title varchar (20), Author varchar (20), Genre varchar (20))"""

#mycursor.execute(tablebooks)

#insert value into table
'''insertvalue1 = """INSERT INTO Books VALUES (101, "Days of the Week", 
"John Blue", "Education")"""

mycursor.execute(insertvalue1)'''

#insert second value into table
insertvalue2 = """INSERT INTO Books VALUES (102, "Power of Learning", 
"Nadia Doolan", "Education")"""

mycursor.execute(insertvalue2)

#VIEWING
mycursor.execute('SELECT * FROM Books')
result = mycursor.fetchall()
conn.commit() 

for row in result: 
    print (row)
    print ("\n")