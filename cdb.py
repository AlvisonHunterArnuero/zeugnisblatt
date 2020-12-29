import sqlite3

# Let us first connect to the DB
conn = sqlite3.connect('database.db')
print("Opened database successfully")

#just in case we had the tables before on this DB, let's drop them
conn.execute('DROP TABLE teachers')
print('Table [ Teachers ] has been dropped successfully!')

conn.execute('DROP TABLE students')
print('Table [ students ] has been dropped successfully!')

#Create both tables from here now
conn.execute('CREATE TABLE teachers(TEACHER_ID TEXT PRIMARY KEY, TEACHER_FULL_NAME TEXT NOT NULL)')
print("Teachers Table created successfully")

#conn.execute('CREATE TABLE students (ID INTEGER PRIMARY KEY AUTOINCREMENT,FIRST_NAME TEXT NOT NULL,LAST_NAME TEXT NOT NULL,FATHER_NAME TEXT NOT NULL,MOTHER_NAME TEXT NOT NULL,PHONE TEXT NOT NULL,AGE INT NOT NULL,GPA REAL, CURRENT_ADDRESS CHAR(50),CITY TEXT NOT NULL,PIN INT NOT NULL,TEACHER_ID TEXT NOT NULL, FOREIGN KEY (TEACHER_ID) REFERENCES teachers(TEACHER_ID))')
conn.execute('CREATE TABLE students (ID INTEGER PRIMARY KEY AUTOINCREMENT,FIRST_NAME TEXT NOT NULL,LAST_NAME TEXT NOT NULL,FATHER_NAME TEXT NOT NULL,MOTHER_NAME TEXT NOT NULL,PHONE TEXT NOT NULL,AGE INT NOT NULL,GPA REAL, CURRENT_ADDRESS CHAR(50),CITY TEXT NOT NULL,PIN INT NOT NULL,TEACHER_ID TEXT NOT NULL)')
print("Student Table created successfully")
#once is done, let's close the connection to the DB
conn.close()
