##ПАТТЕРНЫ ПРАУКТИРОВАНИЕ
##ПОРАЖДАЮЩИЕ(Singleton, Fabric, Abstract Fabric)
##СТРУКТУРНЫЕ(Facade)
##ПОВЕДЕНЧИСКИЕ(Iterator)
#
##Создайте классическую реализацию паттерна Singleton.
##Протестируйте работу созданного класса.
##__init - команда определения экземпляра __new__ - команда-конструктор
#
#class Singleton:
#    _instsnce = None
#    def __new__ (cls):
#        if cls._instsnce is None: # если экземпляра одниночки нет
#            cls._instsnce = super(Singleton, cls).__new__(cls)  # создать экземпляр одиночку
#        else:
#            print('Экземпляр-одиночка уже создан')
#        return cls._instsnce
#    
#class NotSingLetone:
#    pass
#
#refery = Singleton()
#print(refery)
#refery2 = Singleton()
#print(refery2)
#print(refery is refery2)
#
#obj1 = NotSingLetone()
#obj2 = NotSingLetone()
#print(obj1 is obj2, obj1, obj2)
#
##pattern Fabric
#
#class Fabric:
#    def __init__(self, name, age, profesia):
#        self.name = name
#        self.age = age
#        self.profesia = profesia
#    def get_infj(self):
#        return f'name:{self.name}, profesia:{self.profesia}'
#    
#
#class Driver(Fabric):
#    def __init__(self, name, age, profesia):
#        super().__init__(name, age, profesia)
#
#class Pilot(Fabric):
#    def __init__(self, name, age, profesia):
#        super().__init__(name, age, profesia)
#
#user1 = Driver('Dominuic Taretto', 45, 'Speedster')
#user2 = Pilot('Alasheev', 76, 'test pilot')
#print(user1, user2)
#print(issubclass( Driver, Fabric), issubclass( Pilot, Fabric) )
#
##
#from abc import ABC, abstractmethod
#class AbstractFactory(ABC):
#    @abstractmethod
#    def create_factory(self,name):
#        if name == 'Lada':
#            factory = LadaFactory()
#            return factory
#        elif name == 'Sukhoi':
#            factory = SukhoiFactory()
#            return factory
#
#class LadaFactory(AbstractFactory):
#    def __init__(self):
#        self.name = 'фабрика компании лада'
#
#class SukhoiFactory(AbstractFactory):
#    def __init__(self):
#        self.name = 'фабрика компании Сухой'
#    def create_factory(self, name):
#        return super().create_factory(name)
#f = SukhoiFactory()
#factory_from_irkutsk = f.create_factory('Sukhoi')
#
#print(factory_from_irkutsk)

#Пользователь вводит с клавиатурынабор чисел и путь
#кфайлу для сохранения полученных данных. Необходимо:
#■ Сохранить все полученные числа.
#■ Найти максимум, минимум. Эти значения сохранить
#в том же файле.
#■ Отобразить числа.
#■ Отобразить максимум и минимум.
#■ Создать класс для логгирования операций. При создании объекта класса нужно уточнить куда производится
#логгирование: экран или файл. В программе можно
#создать только один объект класса. Все действия
#объекта этого класса.

class Logger:
    _instance = None
    logger_location = None
    def __new__(cls):
        if cls._instance is None:
            cls.logger_location = input('куда вести запись логирования:\n 1-в файл\n 2-в терминал')
            cls._instance = super(Logger, cls).__new__(cls)
        else:
            print('лщгер уже создан')
        return cls._instance
    
    def logging(self, message):
        if self.logger_location == '2':
            print(message)
        else:
            with open('Logging.txt', 'a', encoding='utf-8') as file:
                file.write(message + '\n')

    def log_input_digits(self):
        self.logging('были добавленны числы')

    def log_extrem_digits(self, maxx, minx):
        self.logging(f'max:{maxx}, min {minx}')

    def log_render(self, list_digits):
        self.logging(f'Выполнен рендер массива {list_digits}, макс. элемента {max(list_digits)} и миню элемента {min(list_digits)}')

class Digits:
    def __init__(self, path = 'Digits.txt', logger = None):
        array = input('введите числа через пробел')
        self.path = path
        self.logger = logger
        self.list_digits = list(map(int, array.split(' ')))
        with open(path, 'a', encoding='utf-8') as file:
            for digit in self.list_digits:
                file.write(str(digit)+'\n')
        logger.log_input_digits()

    def grt_extrem(self):
        maxx = max(self.list_digits)
        minx = min(self.list_digits)
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(f'максимальный элемент {maxx}, минимальный {minx}' )
        self.logger.log_extrem_digits(maxx, minx)
        
    def render(self):
        print(f'массив чисел: {self.list_digits}. \nMax {max(self.list_digits)}, min: {min(self.list_digits)}')
        self.logger.log_render(self.list_digits)
logger = Logger()
print(logger)
array = Digits(logger=logger)
array.grt_extrem()
array.render()