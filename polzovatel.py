#Необходимо разработать приложение, которое позволит сохранять информацию о логинах пользователей и их
#паролях. Каждому пользователю соответствует пара ло-
#■ Добавить нового пользователя
#■ Удалить существующего пользователя
#■ Проверить существует ли пользователь
#■ Изменить логин существующего пользователя
#■ Изменить пароль существующего пользователя
#Для реализации задания обязательно используйте
#одну из структур данных. При выборе руководствуйтесь
#постановкой задачи.


class User:
    def __init__(self, login, password, next_user = None):
        self.login = login
        self.password = password
        self.next_user = next_user


class UserBase():
    head = None
    length = 0
    def __str__(self):
        line = f'Список пользователей:\n'
        current_user = self.head
        for i in range(self.length):
            line += f'login: {current_user.login}, password: {current_user.password}\n'
            current_user = current_user.next_user
        return line
    def my_append(self, user):
        if self.head is None:
            self.head = user
        else:
            user.next_user = self.head
            self.head = user   
        self.length += 1

    def search_of_login(self, login):
        current_user = self.head
        prev_user = None
        for index in range(self.length):
            if login == current_user.login:
                return current_user, prev_user
            else:
                prev_user = current_user
                current_user = current_user.next_user
        else:
            return None
        
    def delete_user(self, login):
        if login == self.head.login:
            current_user = self.head
            self.head = self.head.next_user
            del current_user
        else:
            current_user, prev_user = self.search_of_login(login)
            prev_user.next_user = current_user.next_user
            del current_user
        self.length -= 1
    def check_user(self, login):
        if self.search_of_login(login) is None:
            return False
        else:
            return True
        
    def update_user(self):
        login = input('что заменить')
        current_user, prev_user = self.search_of_login(login)
        if current_user is None:
            print('нет такого пользователя')
        else:
            new_login = input('введите новый логин')
            current_user.login = new_login

    


array = UserBase()

user1 = User('lina', '123465')
user2 = User('Dag', '777')
user3 = User('lolita', '7012377')
array.my_append(user1)
array.my_append(user2)
array.my_append(user3)
print(array.search_of_login('Dag'))
#print(array.delete_user('lolita'))
print(array.update_user())
print(array)