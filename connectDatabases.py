import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mycursor.execute("CREATE Table if not exists  test1.testtable1(C1 int, C2 int)")
mycursor.execute("insert into test1.testtable1 values(123,456)")
mycursor.execute("insert into test1.testtable1 values(1234,4567)")
mycursor.execute("insert into test1.testtable1 values(12356,45678)")
mycursor.execute("Select * from test1.testtable1")
for i in mycursor.fetchall():
    print(i) 
mycursor.execute("Select c1 from test1.testtable1")
for i in mycursor.fetchall():
    print(i) 
mycursor.close()