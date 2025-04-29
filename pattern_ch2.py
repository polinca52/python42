#FACADE - суть паттерна в объединении структуры классов в один интерфейс
# Создайте реализацию паттерна Facade. Протестируйте
#работу созданного класса.
#Симулировать выпуск цифрового продукта. Продукт является 
# результатом действия трех составных: дизайн, программирование, тестирование

#class Designe:
#    def get_designe():
#        return f'результат деятельности отдела дизайна'
#    
#class Programmer:
#    def get_programmer():
#        return f'результат деятельности отдела разработчиков'
#    
#class Tester:
#    def get_tester():
#        return f'результат деятельности отдела тестирования'
#    
#class WebStudio: #наш фасад
#    def __init__(self, name):
#        self.name = name
#
#    def get_designe(self):
#        return Designe.get_designe()    
#
#web_stodio = WebStudio('студия цифровых продуктов')
# 
#print(web_stodio.get_designe())


#Adapter - позволяет несовместимым объектам работат вместе
#Создайте реализацию паттернаAdapter. Протестируйте
#работу созданного класса. Есть два кашелька в rub  и tng, нужно сделать адаптер для конвертации валют

#class WalletRub:
#    def __init__(self, cashe):
#        self.cashe = cashe
#
#    def check_balance(self):
#        print(f'{self.cashe} RUB')
#
#class WalletTng:
#    def __init__(self, cashe):
#        self.cashe = cashe    
#    
#    def check_balance(self):
#        print(f'{self.cashe} TNG')
#
#class AdapterRubTng:
#    def __init__(self, cashe):
#        self.cashe = cashe * 6.26
#
#    def check_balance(self):
#        print(f'{self.cashe} TNG')
#
#my_wallet_ru = WalletRub(100)
#my_wallet_ru.check_balance()
#
#kzt_freund_tng =  WalletTng(12)
#kzt_freund_tng.check_balance()
#
#my_wallet_kzt = AdapterRubTng(my_wallet_ru.cashe)
#my_wallet_kzt.check_balance()

#strategy
#


#class User:
#    def __init__(self):
#        pass
#
#    def start(self, strategy):
#        print(strategy)
#
#class StrategyA:
#    list_product = ['площадь 20кв.м', 'площадь 230 кв.м']
#    def strategy():
#        return StrategyA.list_product
#
#class StrategyB:
#    list_product = ['площадь 24000кв.м', 'площадь 30000 кв.м']
#    def strategy():
#        return StrategyB.list_product
#    
#user = User()
#user.start(StrategyA.strategy())
#print('2 hours later')
#user.start(StrategyB.strategy())

#iterator позволяет итерировать (перебирать) элементы объекта класса сохраняя все принципы инкапсуляции
#Есть список (каталог) товаров, создать класс и метод вывода каталога товаров

#class Market:
#    def __init__(self, list_product):
#        self.list_product = list_product
#        self.index = 0
#
#    def __iter__(self):
#        return self
#    
#    def __next__(self):
#        if self.index < len(self.list_product):
#            product = self.list_product[self.index]
#            self.index += 1
#            return product 
#        else:
#            raise StopIteration
#        
#products = ['чокопай', ' орео', 'тук']
#wb = Market(products)
#for product in wb:
#    print(product)


class Group:
    def __init__(self, name):
        self.list_student = []
        self.name = name
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.list_student):
            product = self.list_student[self.index]
            self.index += 1
            return product 
        else:
            raise StopIteration
    
    def add_student(self, name, age):
        self.list_student.append(Student(name, age))
        print('студент  добавлен')

    def delete_student(self, name_student):
        for index_student in range(len(self.list_student)):
            if self.list_student[index_student].name == name_student:
                student = self.list_student[index_student]
                self.list_student.pop(index_student)
                del student  
                return self.list_student
    
    def update(self, new_name):
        new_name = input('введите новое название групы')
        self.name = new_name
        return self
    def render_group(self):
        print(f'group "{self.name}"')
        num = 0
        for student in self.list_student:
            num += 1
            print(f'{num}. {student.name}, age {student.age}')
            

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def update(self):
        menu = input('обновить\n 1-имя\n 2-возраст')
        new_info = input('введите новое значение')
        if menu == '1':
            self.name = new_info
        else:
            self.age = int(new_info)

class Academy:
    def __init__(self, name):
        self.list_group = []
        self.name = name
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.list_group):
            product = self.list_group[self.index]
            self.index += 1
            return product 
        else:
            raise StopIteration
    
    def add_group(self, name):
        self.list_group.append(Group(name))
    
    def delete_group(self, name_group):
       for index_group in range(len(self.list_group)):
           if self.list_group[index_group].name == name_group:
               group = self.list_group[index_group]
               self.list_group.pop(index_group)
               del group  
               return self.list_group
           
    def add_student(self, name_group, name_student, age_student ):
        for group in self.list_group:
            if name_group == group.name:
                group.add_student(name_student, age_student)

    

academy = Academy('TOP')

while True:
    print('МЕНЮ')
    menu = input('1-добавить группу\n2-добавить студента в группу\n3-вывод групп\n4-вывод списка групп\n5-удалить группу\n6-удалить студента\n7-изменить инфо группы\n8-изменить инфо студентов\n0-выход')
    if menu == '1':
        name_group = input('введите название группы')
        academy.add_group(name_group)
    elif menu == '2':
        info = input('ввудите название группы, имя студента, возраст, через запятую')
        name_group, name_student, age_student = info.split(',')
        academy.add_student(name_group, name_student, age_student)
    elif menu == '3':
        print(f'академия {academy.name}')
        for group in academy:
            print(group.name)
    elif menu == '4':
        name_group = input('введите название группы')
        for group in academy:
            if group.name == name_group:
                group.render_group()
                break
            else:
                print('такой группы нет')
    elif menu == '5':

        name_group = input('введите название группы')
        academy.delete_group(name_group)

    elif menu == '6':
        name_group, name_student = input('введите название группы и имя студента через запятую').split(',')
        for group in academy:
            if group.name == name_group:
                group.delete_student(name_student)
                break
        else:
             print('такой группы нет')
        
    elif menu == '7':
        name_group = input('введите  название групы')
        new_name_group = input('введите новое название групы')
        for group in academy:
            if group.name == name_group:
                group.update(new_name_group)
               
       

    elif menu == '8':
        name_group, name_student = input('введите название группы и имя студента через запятую').split(',')
        for group in academy:
            if group.name == name_group:
                for student in group:
                    if name_group == student.name:
                        student.update()

               
               
    else:        
        break


#std1, std2, std3 = Student('Proskovia', 100), Student('Galina', 3), Student('Akakia', 30)
#top = Academy('top')
#top.add_group('python42')
#top.add_group('WEB42')
#top.add_group('52')
##top.delete_group('52')
#top.add_student('python42', 'Proskovia', 100 )
#top.add_student('WEB42', 'Galina', 3 )
#top.add_student('52', 'Akakia', 30 )
#top.add_student('python42', 'Max', 1 )
#top.add_student('WEB42', 'Dima', 323 )
#top.add_student('52', 'Polina', 17 )
#for group in top:
#    print(group.name)
#    group.render_group()
#
#print(std1.__dict__, std2.__dict__, std3.__dict__)    
#group1 = Group('python42')
#group1.add_student(std1)
#group1.add_student(std2)
#group1.add_student(std3)

#group1.delete_student('Akakia')
#group1.render_group()
#print('группа', group1.name)
#for student in group1:
#    print(student.name, student.age)

