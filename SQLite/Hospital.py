import sqlite3 as s 
from generator import hospital_info

with s.connect('python42/SQLite/Hospital.db') as db:
    cursor = db.cursor()
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Departments(
#                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                   building INTEGER NOT NULL CHECK(building>=1 AND building <= 5),
#                   name TEXT NOT NULL UNIQUE)               
#''')
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Doctors(
#                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                   phone INTEGER NOT NULL ,
#                   name TEXT NOT NULL ,
#                   salary REAL NIT NULL)               
#''')
#    cursor.execute('''
#CREATE TABLE IF NOT EXISTS Wards(
#                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                   building INTEGER NOT NULL CHECK(building>=1 AND building <= 5),
#                   floor INTEGER NOT NULL CHECK(floor >=  1) ,
#                   number INTEGER NOT NULL
#                   )               
#''')
#    for i in hospital_info[0]:
#        cursor.execute('''
#    INSERT INTO Departments(building, name) VALUES (?, ?)                 
#''', (*i,))
#        
#    for i in hospital_info[1]:
#        cursor.execute('''
#    INSERT INTO Doctors(name, phone, salary) VALUES (?, ?, ?)                  
#''', (*i,))
#    for i in hospital_info[2]:
#        cursor.execute('''
#    INSERT INTO Wards(building, floor, number) VALUES (?, ?, ?)                  
#''', (*i,))
    cursor.execute('''
 SELECT name, salary FROM Doctors WHERE salary > 50000
''')
    black_list = cursor.fetchall()
    for person in black_list:
        print(person)
    
    cursor.execute('''
 SELECT * FROM Doctors WHERE name LIKE 'A%'
''')
    black_list = cursor.fetchall()
    for person in black_list:
        print(person)
    
    cursor.execute('''
 SELECT name FROM Departments WHERE building = 1 OR building=2
''')
    black_list = cursor.fetchall()
    for person in black_list:
        print(person)

    cursor.execute('''
 SELECT number FROM Wards WHERE (building = 1 OR building=2) AND floor = 2
''')
    black_list = cursor.fetchall()
    for person in black_list:
        print(person)

