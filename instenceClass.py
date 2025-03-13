'''class MyClass:
    def example_method(self):
        print('метод зкземпляра класса')

    @staticmethod #статический - значение принадлежащие только классу (не экземпляром)
    def static_method(name):
        print('Статический метод класса', name)

obj = MyClass()
obj.example_method()
MyClass.static_method()
obj.static_method()

class User:
    def __init__(self, name, last_name, mobile, email, age):
        self.name = name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
        self.age = age

    def other_method(self):
        print("некоторый метод")

class Student(User):
    def __init__(self, name, last_name, mobile, email, age, group):
        super().__init__(name, last_name, mobile, email, age)
        self.group = group

    def lesson(self):
        print('придти на занятие')

class Teacher(User):
    def __init__(self, name, last_name, mobile, email, age):
        super().__init__(name, last_name, mobile, email, age)

    def lesson(self):
        print('провести занятие')

student =Student('Joe', 'Byden', '+1 123 456 78 566', 'poqwei@mail.ru', 77, ' python')
print(student.__dict__)
student.lesson()

teacher =Teacher('Mister', 'Krugj', '+1 123 456 78 566', 'poqwei@mail.ru', 52)
print(teacher.__dict__)
teacher.lesson()'''

#функция issubclass()
'''print(issubclass(Student, User))'''

#функция isinstance
'''print(isinstance(student, Student))
print(isinstance(teacher, Student))
print(isinstance(student, User))'''

#1
'''class Person:
    count = 0

    @staticmethod
    def get_count():
        print(f'кол во созданных экзепляров {Person.count}')

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


obj1 = Person()
obj2 = Person()
Person.get_count()
obj3 = Person()
Person.get_count()'''

#2
'''class Figure:
    count = 0
    def __init__(self,name, *l):
        self.name = name.lower()
        self.lenght = l

    def s(self):
        if self.name == 'треугольник':
            p = sum(self.lenght)/2
            a = self.lenght[0]
            b = self.lenght[1]
            c = self.lenght[2]
            self.square = (p *(p-a)*(p-b)*(p-c))**0.5
            Figure.count += 1
        elif self.name == 'прямоугольник':
            a = list(set(self.lenght))[0]
            b = list(set(self.lenght))[1]
            self.square = a * b
            Figure.count += 1
        elif self.name == 'квадрат':            
            self.square = self.lenght[0] **2
            Figure.count += 1
        elif self.name == 'ромб':
            self.square = self.lenght[0] * self.lenght[1] * 0,5
            Figure.count += 1
        else:
            print('некорректнфй ввод')
    @staticmethod
    def get_count():
        print(f'кол во созданных экзепляров {Figure.count}')

figure = Figure('треугольник', 1, 2, 3)
figure2 = Figure('квадрат',5, 5, 5, 5)
figure.s()
figure2.s()
Figure.get_count()'''

#3
'''class MathClass:
    @staticmethod
    def max(a, b, c, d):
        print(max(a, b, c, d))

    @staticmethod
    def min(a, b, c, d):
        print(min(a, b, c, d))

    @staticmethod
    def average(a, b, c, d):
        print(sum([a, b, c, d]) / 4)

    @staticmethod
    def fact(a):
        fact = 1
        while a != 1:
            fact *= a
            a -= 1
        print(fact)

MathClass.max(23, 34, 67, 12)
MathClass.min(12, 34, 76, 52)
MathClass.average(1, 2, 4, 1)
MathClass.fact(5)'''

#4
'''
class Human:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def work(self):
        print('*работают работу*')

class Builder(Human):
    def __init__(self, name, last_name, age, company):
        super().__init__(name, last_name, age)
        self.company = company
    def process(self):
        print('строит')

class Sailor(Human):
    def __init__(self, name, last_name, age, ship):
        super().__init__(name, last_name, age)
        self.ship = ship
    def process(self):
        print('ходит по воде')

class Pilot(Human):
    def __init__(self, name, last_name, age, plane):
        super().__init__(name, last_name, age)
        self.plane = plane
    def process(self):
        print('летает')

builder = Builder('Иван', 'Иванов', 34, ' русмострой')
sailor = Sailor('петр', 'петров', 34, ' титаник')
pilot = Pilot('сергей', 'сергеев', 34, ' Boing 800 - 830')
builder.process()
sailor.process()
pilot.process()'''

#5
'''
class Passport:
    def __init__(self, name, last_name, bod, country, number):
        self.name = name
        self.last_name = last_name
        self.bod = bod
        self.country = country
        self.number = number

class ForeignPassport(Passport):
    def __init__(self, name, last_name, bod, country, number, ):
        super().__init__(name, last_name, bod, country, number)
        self.visa = {}
    def open_visa(self, location):
        self.visa[location] = True
    def close_visa(self,location):
        self.visa[location] = False

person = ForeignPassport('Иван','иванов', '30-04-08', 'РФ', '1230984567')
person.open_visa('Amerika')
person.open_visa('China')
print(person.visa)
person.close_visa('China')
print(person.visa)'''

#6
class Animal:
    def __init__(self, title, tip, wool,habitat):
        self.title =title
        self.tip = tip
        self.wool = wool
        self.habitat = habitat
class Tigr(Animal):
    def __init__(self, title, tip, wool, habitat, ):
        super().__init__(title, tip, wool, habitat)
      
    def voise(self):
        print('рррррррр')

class Krokodil(Animal):
    def __init__(self, title, tip, wool, habitat):
        super().__init__(title, tip, wool, habitat)
        
    def voise(self):
        print('не говорящий')

class Kangaroo(Animal):
    def __init__(self, title, tip, wool, habitat, hobby):
        super().__init__(title, tip, wool, habitat)
        self.hobby = hobby
        
    def voise(self):
        print('не говорящий')

animal = Kangaroo('просковья','холерик','есть шерсть', 'зоопарк', 'бокс')
print(animal.__dict__)