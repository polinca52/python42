from Model import User
def render(list_user):
    num = 1
    print('список пользователей:')
    for user in list_user:
        print(f'{num}. {user.name};')
        num += 1
def menu(list_user, path):
    while True:
        menu = input('Menu:\n1-вывод списка пользователей\n2-добавить пользователя\n3-сохранить\n0-выход')
        if menu == '1':
            render(list_user)
        elif menu == '2':
            name = input('введите имя пользователя')
            list_user.append(User(name))
        elif menu == '3':
            with open(path, 'a') as file:
                for user in list_user:
                    file.write(user.name + '\n')
        elif menu == '0':
            break
            