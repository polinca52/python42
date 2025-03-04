# Команды ввода\вывода
"""

# комментарий
'''comment'''

#команда вывода print('message1','message2', end='что в конце', sep='знак отделения')
print('hello', 'World','!', sep='***') #\n(new_line, новая строка) \t(табуляция)

#команда ввода input()
# + любая буква(рекомендуется строчная), _ , цифра(НО не первая)
# пример хорошего нэйминга a, men32, user_name, _sum, max_
# - ",'+=@$/>...
var = input('Введите значение переменной ')
print(var)

"""# Литералы

##Типы данных
"""

# целочисленный integer int()
a = 50
b = 50_000
bin_ = 0b101010 # 0b - префикс двоичного числа
oct_ = 0o52 # 0o - префикс двоичного числа
hex_ = 0x2A # 0x - префикс двоичного числа
print(type(a), type(b), bin_, oct_, hex_, type(int('52')), int('101010',2))

# вещественные числа (числа с плавающей точкой) float, float()
a = 5.5
b = .7
print(a, b, type(a), type(b), float(4), 4.)

# cтроки string, str()
a = 'hello'
b = "world"
d = '42'
#print(a * 5, b, d + '11', type(a), type(d))
print(f'Мое {a} любимое число{42}')

# логический Boolean bool()
a = True
b = False
print(type(a), b)
print(bool(-8), bool('a'), bool([1]))
print(bool(0), bool(''), bool([]))

# None
d = None
print(d)

"""## Математические операторы"""

# Умножение
print(3 * 4)
print(3. * 4)
print(3. * 4.)
print('i'* 52)
print(False * 32)

# Сумма
print(3 + 4)
print(3. + 4)
print(3. + 4.6)
print('i' + '52')
print(True + 32)

# Разность
print(3 - 4)
print(3. - 4)
print(3. - 4.6)
print(True - 32)

# Частное
print(8 / 4)
print(3. / 4)
print(3. / 4.6)
print(True / 32)

# возведение в степень
print(8 ** 4)
print(3. ** 4)
print(3. ** 4.6)
print(3 ** 4.6)

# Деление без остатка
print(8 // 4)
print(9. // 4)
print(3. // 4.6)
print(True // 32)

# остаток от деления
print(8 % 4)
print(9. % 4)
print(3. % 4.6)
print(True % 32)
print(-12 % 10)
a = 3
a *= 2
a //= 3
a -= 1
print(a)

# Приоритетность действий
print(3 * (4 + 2) **3) # по правилам математики

# Условный оператор
"""

#if условие:
#  инструкция1
#
#elif условие:
#  инструкция2
#else:
#  инструкция3

a = 52
if a > 50:
  print(1)
elif 30 < a < 50:
  print(2)
else:
  print(3)

# and ('И')
# or ('ИЛИ')
# not ('НЕ')
# == равно
# != не равно
# >, <, >=, <= больше меньше больше-равно меньше-равно
print('1 == 1', 1 == 1)
print('1 != 1', 1 != 1)
print('1 > 1', 1 > 1)
print('1 >= 1', 1 >= 1)
print(bool(1.6)) #True
print('True and True', True and True)
print('False and True', False and True)
print('False and False', False and False)

print('True or True', True or True)
print('False or True', False or True)
print('False or False', False or False)

print('not False', not False)

Человек уедет домой, если время до 21, есть билет или деньги и нет багаж"""

time = int(input())
ticket = True
many = False
baggage = True
if time < 21 and (ticket == True or many == True) and baggage == False:
  print('Go!')
else:
  print('No go!')