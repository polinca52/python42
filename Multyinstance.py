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

class Square:
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
figure2.check_area()