from model import Film 

def menu(list_films):
    while True:
        menu = input('Menu:\n1-вывод фильмов\n2-добавить фильм\n0-выход')
        if menu == '1':
            for film in list_films:
                film.render()
                choice = input('1-следующий, 0-выход ')
                if choice == '1':
                    continue
                else:
                    break
        elif menu == '2':
            list_films.append(Film('test','test','test','test','test','test','test'))
        else:
            break


        