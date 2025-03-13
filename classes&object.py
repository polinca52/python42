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
'''class Cite:
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
user1.update_info()'''

#class Fraction:
#    def __init__(self, numerator = None, denominator = None):
#        self.numerator = numerator
#        self.denominator = denominator
#
#    def set_fraction(self):
#        self.numerator = int(input('введите знаменатель '))
#        self.denominator = int(input('введите числитель '))
#
#    def get_numerator(self):
#        print(f'числитель: {self.numerator}')
#
#    def get_denominator(self):
#        print(f'знаменатель: {self.denominator}')
#
#    def reduction(self, numerator, denominator):
#        for dit in range(min(numerator, denominator), 1, -1):
#            if numerator % dit == 0 and denominator % dit == 0:
#                print(dit)
#                denominator = denominator // dit
#                numerator = numerator // dit
#        self.denominator = denominator 
#        self.numerator = numerator 
#
#
#    def summ(self):
#        other_numerator = int(input('введите знаменатель 2ой дроби '))
#        other_denominator = int(input('введите числитель 2ой дроби '))
#        summ_numerator = self.numerator * other_denominator + self.denominator * other_numerator
#        summ_denominator = self.denominator * other_denominator
#        self.reduction(summ_numerator, summ_denominator)
#      
#        
#
#    def minus(self):
#        other_numerator = int(input('введите знаменатель 2ой дроби '))
#        other_denominator = int(input('введите числитель 2ой дроби '))
#        summ_numerator = self.numerator * other_denominator - self.denominator * other_numerator
#        summ_denominator = self.denominator * other_denominator
#        self.reduction(summ_numerator, summ_denominator)
#      
#
#    def multplay(self):
#        other_numerator = int(input('введите знаменатель 2ой дроби '))
#        other_denominator = int(input('введите числитель 2ой дроби '))
#        summ_numerator = self.numerator  * other_numerator
#        summ_denominator = self.denominator * other_denominator
#        self.reduction(summ_numerator, summ_denominator)
#    
#    def division(self):
#        other_numerator = int(input('введите знаменатель 2ой дроби '))
#        other_denominator = int(input('введите числитель 2ой дроби '))
#        summ_numerator = self.numerator * other_denominator 
#        summ_denominator = self.denominator * other_numerator
#        self.reduction(summ_numerator, summ_denominator)
#
#
#
#first_fraction = Fraction(3, 4)
#first_fraction.multplay()
#first_fraction.get_numerator()
#first_fraction.get_denominator()


#ИНКАПСУЛЯЦИЯ
# процедурный метод
stack_list = []

def add(stack, elemnt):
    stack.append(elemnt)
    return stack

def delete(stack):
    element = stack[-1]
    stack.pop(-1)
    return element

add(stack_list, 1)
add(stack_list, 2)
print(add(stack_list, 3))
print(delete(stack_list))
print(delete(stack_list))
print(delete(stack_list))

#ООП
#class Stack:
#    def __init__(self):
#        self.stack_list = []
#
#    def add(self, elemnt):
#        self.stack_list.append(elemnt)
#    
#     
#    def delete(self):
#        self.element = self.stack_list[-1]
#        self.stack_list.pop(-1)
#
#my_stack = Stack()
#my_stack.add(1)
#my_stack.add(2)
#my_stack.add(3)
#print(my_stack.stack_list)
#my_stack.delete()
#print(my_stack.stack_list)
#my_stack.delete()
#print(my_stack.stack_list)
#my_stack.delete()

#наследование
class MyClass:
    count = 0
    def __init__(self, name):
        self.name = name 
        MyClass.count += 1
        self.id = MyClass.count

obj1 = MyClass('1ый')
obj2 = MyClass('2ый')
obj3 = MyClass('3ый')
print(MyClass.count, obj1.id, obj2.id, obj3.id)

#ПОЛИМОРФИЗМ
#перегрузка метода с разным типом данных
class Auto:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
    def __str__(self):
        return f'Auto {self.manufacturer}, model {self.model}'
    
example_auto = Auto('lada', 2107)
example_auto2 = Auto('tesla', 'E')
print(example_auto)
print(example_auto2)

#перегрузка с разным количеством параметров
#условия: вводят данные стороны, нужно посчитать площадь фигуры. иначе вывести сообщение об ошибки
class Figure:
    def __init__(self, *l):
        self.lenght = l

    def s(self):
        if len(self.lenght) == 3:
            p = sum(self.lenght)/2
            a = self.lenght[0]
            b = self.lenght[1]
            c = self.lenght[2]
            self.square = (p *(p-a)*(p-b)*(p-c))**0.5
        elif len(self.lenght) == 4:
            a = list(set(self.lenght))[0]
            b = list(set(self.lenght))[1]
            self.square = a * b
        else:
            print('некорректнфй ввод')

figure = Figure(25, 25, 49)
figure2 = Figure(5, 5, 2, 2)
figure.s()
figure2.s()

print(figure.square, figure2.square)

