import sqlite3 as sq

with sq.connect('example.db') as db:# открытие потока на БД
    cursor = db.cursor() #курсор - объект связывающий БД и интерпритатор
    #создание БД
    #cursor.execute('''CREATE TABLE IF NOT EXIST first_db(
    #               id INTEGER
    #               name TEXT)''') # SQL ЗАПРОС
#получение данныч из ДБ
    #cursor.execute('''SELECT * FROM journal''')
    #journal = cursor.fetchall()
    #print(journal)
    ###Task 1
    #for student in journal:
    #    print(f'name:{student[0]}\nAge: {student[1]}\nAver{student[2]}')
    ##task 2
    #cursor.execute('SELECT фио FROM journal')
    #name_list = cursor.fetchall()
    #for name in name_list:
    #    print(name)
    ###task 3
    #cursor.execute('SELECT ср_оценка FROM journal')
    #name_list = cursor.fetchall()
    #for name in name_list:
    #    print(name)
    #task 4
    cursor.execute('SELECT фио FROM journal WHERE оценка > 3')
    name_list = cursor.fetchall()
    for name in name_list:
        print(name[0])
