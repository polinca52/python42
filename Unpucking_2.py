# PICKLE and JSON
# запись в файл dump(что выгрузить, куда выгрузить)
# загрузка из файла load (откуда выгрузка)

#class MyClass:
#    def __init__(self, attr1, attr2, attr3):
#        self.attr1 = attr1
#        self.attr2 = attr2
#        self.attr3 = attr3
#
#from pickle import dump, load
#path = 'C:/python42/My_File.pkl'
##obj1 = MyClass(23,'Python', [234, 'Hello!', True])
#with open(path,'rb') as file:
#    #dump(obj1, file)
#    obj2 = load(file)
#print(obj2.__dict__)
#Создайте класс «Самолет».Наполните его необходимыми характеристиками и методами.
#Реализуйте упаковку и
#распаковку объектов класса «Самолет» с использованием
#модуля pickle
#from pickle import dump, load
#
#class Airplane:
#    def __init__(self, type, class_airplane, passancer, capacity, engine, model):
#        self.type = type
#        self.class_airplane = class_airplane
#        self.passancer = passancer
#        self.capacity = capacity
#        self.model = model
#        self.engine = engine
#    def raise_chassi(self):
#        print(f'{self.model}  lifted the chaussy')
#
#    def lower_class(self):
#        print(f'{self.model} lowered their chausses')
#
#    def start_engine(self):
#        print(f'{self.engine} the engines are running successfully')
#def loader(file):
#    try:
#        while True:
#            yield load(file)
#    except:
#        pass
#
#list_airplane = []
#path = 'C:/python42/Airplane.pkl'   
#while True:
#    for airplane in list_airplane:
#        print(airplane.model)
#    choise = input('1 - add airplane\n2 - save to file\n3 - load from file')
#    if choise == '1':
#        type = input('input type')
#        class_airplane =  input('input class_airplane')
#        passancer =  input('input passancer')
#        capacity =  input('input capacity')
#        model =  input('input model')
#        engine = input('input engine')
#        airplane = Airplane(type, class_airplane, passancer, capacity, engine, model)
#        list_airplane.append(airplane)
#    elif choise == '2':
#        with open(path, 'ab') as file:
#            for airplane in list_airplane:
#                dump(airplane, file)
#        list_airplane.clear()
#    elif choise == '3':
#        with open(path, 'rb') as file:
#            for airplane in loader(file):
#                print(airplane.model)
#            list_airplane.append(airplane)


# JSON
# запись в файл dump(что выгрузить, куда выгрузить)
# загрузка из файла load (откуда выгрузка)
class MyClass:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
    
    def toJSON(self):
        return json.damps(self, indent = 4)

import json
path = 'C:/python42/My_File.pkl'
obj1 = MyClass(23,'Python', [234, 'Hello!', True])
with open(path,'rb') as file:
    json.damp(obj1.toJSON(), file)

            