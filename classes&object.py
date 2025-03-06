#пример "простого" класса
'''class MyFirstClass:
    pass
my_first_object = MyFirstClass()
print(my_first_object)
print(x for x in range(10))'''

#class MyClass:
#    parent = 'MyClass'
#    '''это мной созданный класс'''  
#    def __init__(self):
#        self.creator = 'joe'
#obj = MyClass()
#print(obj.__dict__)
#obj.date = '06_03_2025'
#print(obj.__dict__)
#obj2 = MyClass()
#obj2.date = '24_03_2025'
#print(obj2.__dict__)

'''class Person:
    def __init__(self):
        self.name = None
        self.bod = None
        self.mobile = None
        self.cite = None
    def set_info(self):
        self.name = input('имя')
        self.bod = input('дата рождения')
        self.mobile = input('номер')
        self.cite = input('город')
    def get_info(self):
        print(f'имя:{self.name}\nдата рождения:{self.bod}\nномер:{self.mobile}\nгород:{self.cite},' )

    def update_info(self):
        change = input('изменить:\n 1-имя\n 2-дата рождения\n 3-номер\n4-город')
        if change == '1':
            self.name = input('новое имя')
        elif change == '2':
            self.bod = input('новая дата рождения')
        elif change == '3':
            self.mobile = input('новый номер')
        elif change == '4':
            self.cite = input('новый город')






user1 = Person()
print(user1.__dict__)
user1.set_info()
user1.update_info()
user1.get_info()'''

#2
class Cite:
    def __init__(self):
        self.Human = None
        self.country = None
        self.mobile = None
        self.cite = None


    def set_human(self):
        self.human = input('кол-во жителей')
    def set_country(self):
        self.country = input('страна')
    def set_mobile(self):
        self.mobile = input('телефонный код региона')
    def set_cite(self):
        self.cite = input('город')


    def get_info(self):
        print(f'страна:{self.country}\nгород:{self.cite}\nкод:{self.mobile}\nкол-во жителей:{self.human},' )

    def update_info(self):
        change = input('изменить:\n 1-страну\n 2-кол-во людей\n 3-код\n4-город')
        if change == '1':
            self.country = input('новая страна')
        elif change == '2':
            self.human = input('новое кол-во людей')
        elif change == '3':
            self.mobile = input('новый код')
        elif change == '4':
            self.cite = input('новый город')






user1 = Cite()
print(user1.__dict__)
user1.set_human()
user1.set_cite()
user1.set_mobile()
user1.set_country()


user1.get_info()
user1.update_info()