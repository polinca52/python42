from generator import list_student
import sqlite3 as sql
#print(list_student)
with sql.connect('python42/SQLite/Journal.db')as db:
    cursor = db.cursor()
#    cursor.execute('''CREATE TABLE IF NOT EXISTS Students(
#                   'id' INTEGER PRIMARY KEY AUTOINCREMENT,
#                   'name' TEXT, 
#                   'age' INTEGER, 
#                   'city' TEXT, 
#                   'counntry' TEXT, 
#                   'mail' TEXT, 
#                   'phone' TEXT, 
#                   'group' TEXT, 
#                   'aver_value' REAL, 
#                   'min_theme' TEXT,
#                   'max_theme' TEXT)''')
#заполнение таблтцы
#    for stdnt in list_student:
#        cursor.execute(''' 
#                   INSERT INTO Students('name', 'age', 'city', 'counntry', 'mail', 'phone', 'group', 'aver_value', 'min_theme', 'max_theme') VALUES(?,?,?,?,?,?,?,?,?,?)''', (*stdnt, ))
#TASK 1
#    cursor.execute('''
#SELECT name FROM Students WHERE AVER_VALUE >3.5 AND aver_value < 4.5''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
#TASK 2
#    cursor.execute('''
#SELECT name, age FROM Students WHERE age >= 20 ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 3
#    cursor.execute('''
#SELECT name, age FROM Students WHERE age >= 18 and age >= 27 ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 4
#    cursor.execute('''
#SELECT name, id FROM Students WHERE name = 'Ivan' ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 5
#    cursor.execute('''
#SELECT name, phone FROM Students WHERE phone LIKE '%888%'''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 6
#    cursor.execute('''
#SELECT name, mail FROM Students WHERE mail LIKE 'g%' ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 2
##TASK 2.1
#    cursor.execute('''
#SELECT name, MIN(aver_value) FROM Students ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 2.3
#    cursor.execute('''
#SELECT DISTINCT city, COUNT(name) FROM Students GROUP BY city ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
##TASK 2.4
#    cursor.execute('''
#SELECT DISTINCT counntry, COUNT(name) FROM Students GROUP BY counntry ''')
#    stds = cursor.fetchall()
#    for std in stds :
#        print(std)
