#Функции

## Базовые определения
"""

#Функция
def name_function(a, b):
  if a > b:
    return f'Max {a}'
  elif b > a:
    return f'Max {b}'
  else:
    return 'Equiv'
print(name_function(21, 12))
#
print(name_function(34, 43))
#
print(name_function(55, 55))

# Процедуры
def my_alarm():
  print('ПРЕДУПРЕЖДЕНИЕ!')

for i in range(50, 71):
  print(i)
  if i > 60:
    print(my_alarm())
print('Набор скорости завершен')

"""##Параметры

### Позиционный
"""

# Функция подсчета периметра 4х угольника
def p(a, b):
  return (a + b) * 2
print(p(3, 4))

"""### Именованные параметры"""

def f(passport=False, visa=False):
  if passport:
    if visa:
      return 'Вы прошли контроль'
    else:
      return 'Вы не прошли контроль из-за визы'
  else:
    return 'Вы не прошли контроль из-за паспорта'
print(f(passport=True, visa=True))
print(f(passport=True))
print(f())
print(f(True, True))

"""### Неизвестное количество параметров"""

def aver(*value):
  summ = 0
  for i in value:
    summ += i
  print(summ / len(value))
#распаковка
a = [4, 5, 4]
print(*a)
#aver(4,5,3)
#aver(3, 3, 3 , 3, 3, 3)

#Напишите функцию, которая отображает на экран
#форматированный текст, указанный ниже:
#“Don't let the noise of others' opinions drown
#out your own inner voice.”
#                           Steve Jobs
def f():
  print("\"Don't let the noise of others' opinions drown\nout your own inner voice\".\n\t\tSteve Jobs")
f()

#Напишите функцию, которая принимает два числа
#в качестве параметра и отображает все нечетные числа
#между ними.
def f(a, b):
  for i in range(a, b + 1):
    if i % 2 > 0:
      print(i)
f(3, 7)

#Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
#Функция принимает в качестве параметра: длину линии,
#направление, символ.
#def f(lenght, direction, symbol):
#  if direction == 'v':
#    for i in range(lenght):
#      print(symbol)
#  else:
#    print('$' * lenght)

def f(lenght, direction, symbol):
  for i in range(lenght):
    if direction == 'v':
      print(symbol)
    else:
      print(symbol, end='')

menu = input('Введите количество,\nнаправление (v-вертикально, h-горзонтально) и\n символ через пробел')
menu = menu.split(' ')
f(int(menu[0]), menu[1], menu[2])

"""## Глобальные и локальные переменные"""

# локальные переменные
def f(a, b):
  summ = a + b
  return summ
a = 5
b = 10
print(a, b)
print(f(a, b))
# print(summ) локальная переменная

def f(a, b):
  summ = a + b + c
  return summ
a = 5
b = 10
c = 20 # глобальная переменная
print(f(a, b))

#glabal
def f(a, b):
  global c
  c = a + b
  return c
a = 5
b = 10
c = 2 # глобальная переменная
print(f(a, b), c)

# nonlocal
def nl():
  a = 1
  def loc():
    global b
    nonlocal a
    print(f'Локальный:{a},{b}')
  return print(f'Нелокальный: {a}'), loc()
a = 0
b = 0
nl()
print(a, b)

#Задание 4
#Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
#параметров.
def f(a, b, c, d):
  return max([a, b, c, d])
print(f(12, 7, 10, 1))

#Напишитефункцию, которая возвращает сумму чисел
#в указанном диапазоне. Границы диапазона передаются
#в качестве параметров.
def f(a, b):
  summ = 0
  for i in range(a, b + 1):
    summ += i
  return summ
print(f(1, 7))

# Напишите функцию, которая проверяет является ли
#число простым. Число передаётся в качестве параметра.
#Если число простое нужно вернуть из метода true, иначе
#false.
def f(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(f(8))
print(f(11))

#Напишите функцию, которая проверяет является
#ли шестизначное число «счастливым». Число передаётвернуть из функции true, иначе false.
#«Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых
#цифр. Например, 123420 – счастливое
def f(n): #функция проверки счастья
    l3, r3 = str(n)[:3], str(n)[3:] # деление 6ти значного на 2 по 3
    if sum_digit(l3) == sum_digit(r3): # проверка счастья
        return True
    else:
        return False

def sum_digit(s): #функция подсчета суммы цифр в числе
    return int(s[0]) + int(s[1]) + int(s[2])

print(f(123420))
print(f(183420))

"""## Оператор yield"""

#1 функция вывода натуральных чисел от 1 до n
def render(n):
  for i in range(1, n + 1):
    return str(i)
s = ''
s += render(5)
print(s)

def render2(n):
  for i in range(1, n + 1):
    yield str(i)
s = ''
for i in render2(5):
  s += i
print(s)
l = [i for i in render2(5)]
print(l)

#2 функция для вывода ряда квадратов от 1 до n
def pow_2(n): # объявление функции
  for i in range(1, n + 1): # цикл натуральных чисел от 1 до n
    yield i ** 2 # многократный возврат квадрата числа
list_power = [i for i in pow_2(10)] #использование функции как генератора
print(list_power) # вывод

# написать функцию поиска первых n чисел фибоначчи
def fib(n):
  a = 1
  b = 1
  for i in range(n - 2):
    p = a + b
    a = b
    b = p
    yield p
list_fib = [1, 1] + [i for i in fib(20)]
print(list_fib)

"""## Рекурсия"""

# создать функцию, которая считает сумму всех натуральных чисел до числа n
# 10 - 10+9+8+7+6+5+4+3+2+1
def summ_num(n):
    if n == 1:
        return 1
    else:
        return n + summ_num(n - 1)
print(summ_num(20))

#функция подсчет факториала
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))

# написать функцию поиска первых n чисел фибоначчи
def fib(n, a = 0, b = 1):
  if n == 1:
    return str(b)
  else:
    return str(b) + ' ' + fib(n - 1, b, a + b)

print(fib(10))

#Задание 1
#Написать рекурсивную функцию нахождения числа n степени x.
def f(n , x):
    if x == 1:
        return n
    else:
        return n * f(n, x - 1)


#Задание 2
#Написать рекурсивную функцию, которая вычисляет
#сумму всех чисел в диапазоне от a до b.
# Пользователь вводит a и b.
def summ_num(a, b): # 3 7
    if a == b:
        return b
    else:
        return b + summ_num(a, b -1) # 6

#Задание 3
#Написать рекурсивную функцию, которая выводит N
#звезд в ряд, число N задает пользователь.
# Проиллюстрируйте работу функции примером.
def f(n):
    if n == 1:
        return '*'
    else:
        return '*' + f(n - 1)
print(f(4))

#Задание 5
#Напишите рекурсивную функцию, которая принимает
# список из 100 целых чисел, полученных случайным
#образом, и находит позицию, с которой начинается
# последовательность из 10 чисел, сумма которых минимальна.
from random import randint
rand_list = [randint(1,10) for i in range(10)]
print(rand_list)
def summ_num(indx_l, indx_r):
    if indx_l == indx_r:
        return rand_list[indx_l]
    else:
        return rand_list[indx_l] + summ_num(indx_l + 1, indx_r)

summ_list = []
for i in range(len(rand_list) - 2):
    print(summ_num(i, i + 2))
    summ_list.append(summ_num(i, i + 2))
print('min_Summ', min(summ_list))
print('index_min_Summ', summ_list.index(min(summ_list)))

#Задание 6
#Написать функцию, которая принимает две даты
#(т.е. функция принимает шесть параметров) и вычисляет
#разность в днях между этими датами. Для решения этой
#задачи необходимо также написать функцию, которая
#определяет, является ли год високосным.
def delta(d1, m1, y1, d2, m2, y2):
    list_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    h_y = 0
    for i in range(y1, y2):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
             h_y +=1
    delta1 = y1 * 365 + sum(list_m[:m1]) + d1
    delta2 = y2 * 365 + sum(list_m[:m2]) + d2
    return delta2 - delta1 + h_y
print(delta(23,1,2024, 23, 1, 2025))

"""#Модули"""

# модуль math
import math
for i in dir(math):
  print(i)
# некоторые объекты модуля
#sin(x) → синус x;
#cos(x) → косинус x;
#tan(x) → тангенс x.
#pi → константа со значением, приближенным к π;
#radians(x) → функция, которая преобразует x из градусов в радианы;
#degrees(x)  → действие в  обратном направлении (от
#радианов к градусам).
#e  → константа со значением, которое приближено
#к числу Эйлера (e);
# exp(x) → нахождение значения ex
# log(x) → натуральный логарифм x;
# log(x, b) → логарифм x по основанию b;
# log10(x)  → десятичный логарифм x (более точный,
#чем log(x, 10));
# log2(x) → двоичный логарифм x (более точный, чем
# log(x, 2));
# pow(x, y) → нахождение значения xy
# (обратите внимание на области определения)
# ceil(x) → верхнее округление x (наименьшее целое число, больше или равное x);
# floor(x)  → нижнее округление x (наибольшее целое
#число, меньше или равное x);
#23
#Полезные модули
#■ trunc(x) → значение x, усеченное до целого числа (будьте
#осторожны — оно не эквивалентно ни верхнему ни
#нижнему округление);
#■ factorial(x) → возвращает x! (x должен быть целым и не
#отрицательным);
#■ hypot(x, y) → возвращает длину гипотенузы прямоугольного треугольника с длинами катетов, равными
#x и y (аналогично sqrt(pow(x, 2) + pow(y, 2)) , но более
#точно).

"""## Способы импорта модуля"""

# 1
import math
print(math.sin(math.pi/2))

# 2
from math import exp
print(exp(1), floor(3.5))

from math import ceil, floor
print(ceil(3.5), floor(3.5))

# 3
from math import*
print(pow(2,7))
print(ceil(3.5), floor(3.5))

# псевдоним
from math import factorial as f
print(f(5), factorial(5))

import random
for i in dir(random):
  print(i)

# игра Висилица
# игра Висилица
from random import choice

def start(list_words):
  random_word = choice(list_words)
  return random_word

def render(random_word):
    word = ''
    for i in random_word:
        word += '_ '
    return word

def check_win(lives, play_word):
    if lives < 1:
        print('Loose!')
        return False
    elif '_' not in play_word:
        print('WIN! CONGRATULATIONs!')
        return False
    else:
        return True

def game(random_word, play_word, lives):
    use_letter = ''
    while True:
        print('Загадано слово:', play_word, f'Жизней осталось {lives}', sep='\n')
        letter = input('Введите букву')
        if letter in use_letter:
            print("Эту букву уже называли!")
        else:
            use_letter += letter
            if letter in random_word:
                new_play_word = ''
                for i in range(len(random_word)):
                    if random_word[i] == letter:
                        new_play_word += letter + ' '
                    else:
                        new_play_word += play_word[i * 2] + ' '
                play_word = new_play_word
                random_word = random_word.replace(letter, '_')
                print('Есть такая буква!', play_word, sep='\n')
            else:
                lives -= 1
                print('Нет такой буквы. Жизней осталось', lives)
        if check_win(lives, play_word) == False:
            break
    print('GAME OVER')

list_words = ['tiger', 'cat', 'pig', 'dog', 'pinguine', 'elephant', 'turtle']
lives = 3
random_word = start(list_words)
play_word = render(random_word)
game(random_word, play_word, lives)

"""#"Магические" функции"""

num_list = ['2', '3', '4', '5']
# map
new_num_list = list(map(int, num_list))
print(new_num_list)
# lambda
for i in map(lambda x: x ** 3, new_num_list):
  print(i)
l = [1000, 900]
l2 = [900,600]
summ = list(map(lambda x, y: x + y * 1.2, l, l2))
print(summ)

"""# Краткий обзор замыкания"""

def out_f():
  var = 1
  def in_f():
    return var
  return in_f()

my_var = out_f()
print(my_var)
