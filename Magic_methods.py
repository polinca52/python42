#магический метод 
'''class My_class:
    def __init__(self,name, value):
        self.name =name
        self.value =value
    
    def __str__(self):
        return f"меня зовут {self.name}"
    
    def __eq__(self, other):
        if isinstance(other, My_class):
            if self.value == other.value:
                return f'разные значения'
            else:
                return f'неравные'
        else:
            return f'это экземпляр другого класса'
        '''
    #математические операции
'''    def __add__(self, other):
        if isinstance(other, My_class):
            return self.value + other.value
        else:
            return f'это экземпляр другого класса'
        
    def __pow__(self, other):
        if isinstance(other, My_class):
            return self.value ** other.value
        else:
            return f'это экземпляр другого класса'
        

obj = My_class('мой класс', 20)
obj2 = My_class('второй класс', -1)
sum = obj + 6
print(obj ** obj2)'''


# при сравнении
    #lt(self, other) — определяет поведение оператора сравнения «меньше», <.
#
    #le(self, other) — определяет поведение оператора сравнения «меньше или равно», <=.
#
    #eq(self, other) — определяет поведение оператора «равенства», ==.
#
    #ne(self, other) — определяет поведение оператора «неравенства», !=.
#
    #gt(self, other) — определяет поведение оператора сравнения «больше», >.
#
    #ge(self, other) — определяет поведение оператора сравнения «больше или равно», >=.


# математические операторы
#   add(self, other) — сложение, оператор +

#   sub(self, other) — вычитание, оператор -
#   
#   mul(self, other) — умножение, оператор *
#   
#   truediv(self, other) — деление, оператор /
#   
#   pow(self, other[, modulo]) — возведение в степень, оператор **

#1
'''class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self,other):
        if isinstance(other, Number):
            return self.value - other.value
        else:
            return f'это экземпляр другого класса'
        
    def __add__(self,other):
        if isinstance(other, Number):
            return self.value + other.value
        else:
            return f'это экземпляр другого класса'
    
    def __mul__(self,other):
        if isinstance(other, Number):
            return self.value * other.value
        else:
            return f'это экземпляр другого класса'
    
    def __truediv__(self,other):
        if isinstance(other, Number):
            return self.value / other.value
        else:
            return f'это экземпляр другого класса'
numb1 = Number(5)
numb2 = Number(3)
sub = numb2 - numb1
sum = numb2 + numb1
mult = numb2  * numb1
delt = numb2 / numb1

print(sub, sum, mult, delt)'''

#2
'''class Fraction:
  
    def __init__(self, numerator = None, denominator = None):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def reduction( numerator, denominator):
        for dlt in range(min(numerator, denominator), 0, -1):
            if numerator % dlt == 0 and denominator % dlt == 0:
                numerator = numerator // dlt
                denominator = denominator // dlt
        return numerator,denominator
       

    def __add__(self, other):
        summ_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        summ_denominator = self.denominator * other.denominator
        result =  Fraction.reduction(summ_numerator, summ_denominator)
        return f'результат суммы {result[0]}/{result[1]}'

    def __sub__(self, other):
        summ_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        summ_denominator = self.denominator * other.denominator
        result =  Fraction.reduction(summ_numerator, summ_denominator)
        return f'результат разности {result[0]}/{result[1]}'

    def __mul__(self,other):
        summ_numerator = self.numerator * other.numerator
        summ_denominator = self.denominator * other.denominator
        result =  Fraction.reduction(summ_numerator, summ_denominator)
        return f'результат произведения {result[0]}/{result[1]}'

    def __truediv__   (self, other):
        summ_numerator = self.numerator * other.denominator
        summ_denominator = self.denominator * other.numerator
        result =  Fraction.reduction(summ_numerator, summ_denominator)
        return f'результат деления {result[0]}/{result[1]}'


frac1 = Fraction(3,4)
frac2 = Fraction(2,6)
sum = frac1 +frac2
sub = frac1 - frac2
mult = frac1 *frac2
divis =frac1 - frac2
print(sum, sub, mult, divis)'''

#3 
'''
class Library:
    def __init__(self, name, addres, book_count):
        self.name =name
        self.addres =addres
        self.book_count =book_count
    def __add__(self, value):
        self.book_count += value
    def __iadd__(self,other):
        self.book_count += other
        return self
    def __isub__(self,other):
        self.book_count -= other
        return self
    def __ly__(self, other):
        if self.book_count < other.book_count:
            return f'в библиотеке {other.name} книг больше'
        else:
            return f'в библиотеке {other.name} книг не больше'
    def __le__(self, other):
        if self.book_count <= other.book_count:
            return f'в библиотеке {other.name} книг не меньше'
        else:
            return f'в библиотеке {other.name} книг  меньше'
    def __gt__(self, other):
        if self.book_count > other.book_count:
            return f'в библиотеке {other.name} книг  меньше'
        else:
            return f'в библиотеке {other.name} книг  не меньше'
        
    def __ge__(self, other):
        if self.book_count <= other.book_count:
            return f'в библиотеке {other.name} книг не больше'
        else:
            return f'в библиотеке {other.name} книг  больше'

    def __eq__(self, other):
        if self.book_count == other.book_count:
            return f'в библиотеке одинаково'
        else:
            return f'в библиотеке разное кол-во '

    def __ne__(self, other):
        if self.book_count != other.book_count:
            return f'в библиотеке разное кол-во '
        else:
            return f'в библиотеке одинаково'
        
 

lib1 = Library('библиотека №1', 'г. Жуковский', 50)
lib2 = Library('библиотека №2', 'г. Москва', 100)
print(lib1 != lib2)
#print(lib1.book_count)
#lib1 + 148
#print(lib1.book_count)
#lib1 += 42
#print(lib1.book_count)
#lib1 -= 42
#print(lib1.book_count)
'''

#4
class Date:
    calendary = {
        '1':31,
        '2':28,
        '3':30,
        '4':30,
        '5':31,
        '6':30,
        '7':31,
        '8':31,
        '9':30,
        '10':31, 
        '11':30,
        '12':31
    }
    def __init__(self,date):
        self.day, self.month, self.year = map(int,date.split('-'))
        self.count_day = Date.get_count_day(self.day, self.month, self.year)

    def get_date(self):
        return f"day {self.day}, month {self.month}, year {self.year}"
    
    @staticmethod
    def get_count_day(day, month, year):
        d = day
        dom = 0
        doy = 0
        while(month - 1) != 0:
            dom += Date.calendary[str(month - 1)]
            month -= 1
        doy = year * 365 + len([x for x in range(1,year) if x % 4 == 0 and (x % 400 == 0 or x% 100 != 0)])
        return d + dom + doy
    def __sub__(self,other):
        return f'{abs(self.count_day - other.count_day)} days'
    
    def __add__(self, value):
        while value != 0:
            if value >= 365:
                self.year += 1
                value -= 365
            elif value + self.day > Date.calendary[str(self.month)]:
                
                value = value+ self.day - Date.calendary[str(self.month)]
                self.day = 0
                self.month += 1
            else:
                self.day =  value + self.day
                value = 0
    
    
now = Date('10-2-2023')
#other = ('30-1-2022')
now + 368
print(now.get_date())

