#class FirstSuper:
#    def __init__(self, a):
#        self.a = a
#    def meth(self):
#        return f'FirstSuper'
#    
#class SecondSuper:
#    def __init__(self, b):
#        self.b = b
#    def meth(self):
#        return f'SecondSuper'
#    
#class Sub(FirstSuper, SecondSuper):
#    def __init__(self,a, c):
#        super().__init__(a)
#        self.c = c
#
#object = Sub(1, 2)
#print(object.meth())
#print(object.m2())
#print(object.a)

#1
'''class Square:
    def __init__(self,a):
        self.a =a
    def s_square(self):
        return self.a **2
class Circle:
    def __init__(self,r):
        self.r = r
    def s_circle(self):
        return 3,14 * (self.r ** 2)
    
class SquaredOffArea(Square, Circle):
    def __init__(self, a, r):
        super().__init__(a)
        Circle.__init__(self,r)
    def check_area(self):
        if self.a == 2* self.r:
            print('окр вписнная')
        else:
            print('окр не вписынная')
figure = SquaredOffArea(4, 2)
figure.check_area()
figure2 = SquaredOffArea(6, 2)
figure2.check_area()'''

#2
'''
class Wheel:
    def __init__(self, d):
        self.d = d
    
class Engine:
    def __init__(self, power, type):
        self.power = power
        self.engine_type = type
    def sound_engine(self):
        if self.engine_type == 'electric':
            return f'shh - shh - shh'
        else:
            return f'jrr-rr-rr'



class Door:
    def __init__(self, color):
        self.door_color = color

class Dodywork:
    def __init__(self,type, color, hatch):
        self.dodywork_type=type
        self.dodywork_color =color
        self.hatch = hatch

class Auto(Dodywork, Engine, Wheel, Door ):
    def __init__(self, dodywork_type, dodywork_color, hatch, power, engine_type, d, door_color, door_count,wheel_count):
        super().__init__( dodywork_type, dodywork_color, hatch)
        Engine.__init__(self, power ,engine_type)
        Wheel.__init__(self, d)
        Door.__init__(self, door_color)
        self.door_count = door_count
        self.wheel_count = wheel_count

    def sound_engine(self):
        return super().sound_engine()

    def signal(self):
        return f'beep - beep'

lada_iskra = Auto('sedan', 'red',False, 160, 'ice', 16, 'red', 4, 5)
print(lada_iskra.__dict__, lada_iskra.sound_engine(), lada_iskra.signal())

tesla_a= Auto('crossover', 'blue',True, 380, 'electric', 17, 'red', 5, 5)
'''
#3
'''
class Pet:
    def __init__(self, nic, coating):
        self.nic=nic
        self.coating =coating
        self.paws = None
        self.sound_contant = None
        self.type = None

    

    def sound(self):
            return  self.sound_contant
    
    def show(self):
            return  self.nic

    def get_type(self):
            return  self.type 



     
class Dog(Pet):
      def __init__(self, nic, coating, paws, sound_contant, type ):
        super().__init__(nic, coating)
        self.paws = paws
        self.sound_contant = sound_contant
        self.type = type

        def sound(self):
                return  super().sound()
        def show(self):
                return  super().show()
        def get_type(self):
                return  super().get_type()

class Hamster(Pet):
        def __init__(self, nic, coating,  paws, sound_contant, type ):
              super().__init__(nic, coating)
              self.paws = paws
              self.sound_contant = sound_contant
              self.type = type
        def sound(self):
                return  super().sound()
        def show(self):
                return  super().show()
        def get_type(self):
                return  super().get_type()

class Cat(Pet):
        def __init__(self, nic, coating,  paws, sound_contant, type ):
              super().__init__(nic, coating)
              self.paws = paws
              self.sound_contant = sound_contant
              self.type = type
        def sound(self):
                return  super().sound()
        def show(self):
                return  super().show()
        def get_type(self):
                return  super().get_type()

class Snake(Pet):
        def __init__(self, nic, coating,  sound_contant, type ):
              super().__init__(nic, coating)
              self.sound_contant = sound_contant
              self.type = type
        def sound(self):
                return  super().sound()
        def show(self):
                return  super().show()
        def get_type(self):
                return  super().get_type()

class Turtle(Pet):
        def __init__(self, nic, coating,  paws,  type ):
              super().__init__(nic, coating)
              self.paws = paws         
              self.type = type
        def show(self):
                return  super().show()
        def get_type(self):
                return  super().get_type()


pet  = Dog('шарик', 'шерсть', '4', 'гав-гав', 'собака')
pet  = Cat('Матроскин', 'шерсть', '4', 'мяу-мяу', 'кошка')
pet  = Snake('каа', 'чешуя', 'шшшшшшшшш', 'змея')
pet  = Turtle ('Рафаэль', 'панцирь', '4', 'черепаха')
print(pet.__dict__, pet.show(),pet.get_type(), pet.sound(), sep = '\n')
'''

#4
#Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию
#о служащем. В случае базового класса это может быть строка
#Создайте от него три производных класса: President,
#Manager, Worker. Переопределите функцию Print() для
#вывода информации, соответствующей каждому типу
#служащего.

#class Employer:
#    def __init__(self, name, year, pol):
#        self.name=name
#        self.year =year
#        self.pol = pol
#        
#        
#class President(Employer):
#    def __init__(self, name, year, pol):
#        super().__init__(name, year, pol)
#        print('This is President class')
#
#        
#class Manager(Employer):
#    def __init__(self, name, year, pol):
#        super().__init__(name, year, pol)
#        print('This is Manager class')
#
#class Worker(Employer):
#    def __init__(self, name, year, pol):
#        super().__init__(name, year, pol)
#        print('This is Worker class')
#
#employer= Manager('коля', '35', 'm')
#print(employer.__dict__)

#вариант 2

#class Employer:
#    def __init__(self, name, year, pol):
#        self.name=name
#        self.year =year
#        self.pol = pol
#    '''Employer'''
#    def print(self):
#        return f'This is {str(self.__class__)[17:-2]} class'
#    def __str__(self):
#        return f"меня зовут {self.name}"
#    def __int__(self):
#         return self.year
#
#    
#class President(Employer):
#    def __init__(self, name, year, pol):
#        super().__init__(name, year, pol)
#
#class Manager(Employer):
#    def __init__(self, name, year, pol):
#        super().__init__(name, year, pol)
#
#class Worker(Employer):
#    def __init__(self, name, year, pol):
#        super().__init__(name, year, pol)
#
#user1 = President('Иван', 32, 'm')
#user2 = Manager('катя', 20, 'ж')
#user3 = Worker('оно', 11, 'ср')
#for user in [user1, user2, user3]:
#    print(int(user))
