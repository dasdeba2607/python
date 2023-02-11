import sqlite3
import traceback, sys

# the following line creates a db file of sqllite and then connects
conn = sqlite3.connect('test.db')

print("test db creation successful")

try:
   conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
   print("table created successfully")
except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        print("table did not create successfully")


conn.execute("DELETE from COMPANY where ID = 1")

conn.commit()

print("Total number of rows deleted :", conn.total_changes)

ctr=1

while ctr < 3:
   try:
      print("Enter record no :", ctr)
      id=input("Enter id")
      name=input("name")
      age=input("age")
      address=input("address")
      salary=input("salary")
      sql_data = (id, name, age, address, salary)
      conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (?, ?, ?, ?, ? )", (sql_data));
      conn.commit()
      print("record inserted successfully :", ctr)
      ctr+=1
   except sqlite3.IntegrityError as e:
      print('INTEGRITY ERROR\n')

cursor = conn.execute("select count(*) from Company")

for r in cursor:
    print("the no of records in table ", r[0])

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")

conn.commit()

print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3])

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

conn.close()
