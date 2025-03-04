"""# Строки"""

a = 'Hello'
b = "Python"
# строка индексируется слева-направо с 0, справа-налево с -1
print(a[0],a[1],a[2],a[3],a[4])
print(a[-1],a[-2],a[-3],a[-4],a[-5])
#print(a, type(b))

# срез substring [start:end:step]
a = 'Hello'
print(a[3:5:1]) # полный пример
print(a[3:5]) # без шага (с шагом 1)
print(a[0:3:1])
print(a[:3]) # от начала до 3
print(a[3:]) # от 3 до конца
print(a[::-1]) # переворот строки
print(a[-3:]) # срез с правого края

b = 2345
print(str(b)[::-1])
# перебор строки
c = 'Hello'
for i in c:
  print(i)
for i in range(len(c)):
  print(c[i])

# экранирование
print('начало\nконец')
print('книга \'Колобок\'')
print('книга \\Колобок')

"""## Методы для изменения регистра строки и содрежимого строки"""

#lower
name = input('input name')
if name.lower() == 'joe':
  print('Hello, master', name.lower())
else:
  print('Error')

#upper
name = input('input name')
if name.upper() == 'JOE':
  print('Hello, master', name.upper())
else:
  print('Error')

# capitalize делает первый символ строки заглавным остальные строчными
name = 'joe'
name2 = 'MARK'
print(name.capitalize(), name2.capitalize())

# title делает первые символы каждого слова в строке с заглавной буквы
a = 'hElLo, wORld!'
print(a.title())

# swopcase меняет регистры на противоположные
a = 'hElLo, wORld!'
print(a.swapcase())

word = 'друг'
new_word = ''
for i in word:
   print(i)
   if i == 'д':
    new_word += 'в'
   elif i == 'у':
    new_word += 'a'
   else:
    new_word += i
print(new_word)
# replace(что меняю, на что меняю, сколько раз)
word = word.replace('д','в')
word = word.replace('у','а')
print(word)
name = 'Cемен'
name = name.replace('е','э',1)
print(name)

"""## Методы поиска подстроки в строке"""

s = 'Hello, world!'
print(s.count('25')) # счетает количество вхождений
print(s.find('l')) # возвращает индекс первого вхождения
print(s.rfind('l')) # возвращает индекс последнего вхождения
print(s.index('o')) # возвращает индекс первого вхождения
print(s.rindex('o')) # возвращает индекс первого вхождения
#поиск отсутствующего символа
print(s.count('25'))
#print(s.find('25')) # -1 это отсутствия такой подстроки
#print(s.index('25')) # вызовет ошибку ValueError: substring not found

"""## Методы проверки начала и окончания строк"""

s = 'Hello, world'
print(s.endswith('d'))
print(s.endswith('g'))
#str.endswith(pattern [, startIndex [, endIndex]]) — определяет, заканчивается ли строка str указанным фрагментом pattern.

s = 'Hello, world'
print(s.startswith('H'))
print(s.startswith('g'))
#str.startwith(pattern [, startIndex [, endIndex]]) — определяет, начинается ли строка str с указанного фрагмента
#pattern.

"""## Методы проверки строк"""

a = '!'
b = 'Game23'
print(a.isalnum())
print(b.isalnum())
#str.isalnum() — проверяет, состоит ли строка str только
#из буквенных и цифровых символов.

a = '23'
b = 'Game'
print(a.isalpha())
print(b.isalpha())
print(a.isdigit())
print(b.isdigit())
#str.isalpha() — проверяет, состоит ли строка str только
#из буквенных символов.
#str.isdigit() — проверяет, состоит ли строка str только
#из цифровых символов (используется для проверки,
#является ли строка str числом).

a = 'Hello'
b = 'hello'
print(a.islower())
print(b.islower())
#str.islower() проверяет, находятся ли все буквенные символы строки str в нижнем регистре (символы строки
#str, которые не являются буквой алфавита — игнорируются данной проверкой).

a = 'HELLO'
b = 'HELLo'
print(a.isupper())
print(b.isupper())
#str.isupper() определяет, находятся ли все буквенные
#символы строки str в верхнем регистре.

a = 'Hello'
b = 'hello'
print(a.istitle())
print(b.istitle())
#str.istitle() проверяет, начинается ли каждое слово строки str с символа в верхнем регистре.

"""## Методы форматирования строк"""

a = 'Hello'
print(a.center(30))
print(a.center(30, '!'))
#str.center(width [, fillchar]) дополняет (расширяет) строку
#str до указанной длины width, возвращаемый результат — расширенная копия строки str. Если параметр
#fillchar указан, то он будет использован, как символ
#заполнения, иначе — отступы заполняются пробелами

a = '234'
print(a.zfill(10))
print(a.zfill(1))
#str.zfill(width) дополняет строку
#слева символами «0» ширины width

"""## Срезы"""

myStr="Python-cool!"
#str[start:end:step]
print(myStr[1:3]) #yt
print(myStr[-5:-2]) #coo
print(myStr[-5:11]) #cool
print(myStr[:6]) #Python
print(myStr[:-1]) #Python-cool
print(myStr[6:]) #-cool!
print(myStr[-5:]) #cool!
print(myStr[::-1]) # !looc-nohtyP

"""## Экранирование"""

print('Hello,\nWorld')
print('Hello,\tWorld')
print('\x23') # кодировка ascii (utf-8)
print('\\')

#Пользователь вводит с клавиатуры строку. Посчитайте количество цифр в строке. Выведите
#количество на экран.
s = 'fd45hgfhg65bvh4323vgdbg'
# 1 cпособ: перебрать символы и проверить, что они  цифры
count_ = 0
for c in s:
  if c.isdigit():
    count_ += 1
print(count_)
# 2 способ: подсчет методом count()
count_ = 0
for i in range(10):
  count_ += s.count(str(i))
print(count_)

#№Задание 3, 4
#Пользователь вводит с клавиатуры строку и символ
#для поиска. Посчитайте сколько раз в строке встречается
#искомый символ. Полученное число выведите на экран.
s = 'fd45hgfhg65bvh4323vgdbg' # тут должен быть input()
c = input('символ для поиска')
summ_1 = 0
for i in s:
  if i == c:
    summ_1 += 1
print(summ_1)
print(s.count(c))

#Задание 5
#Пользователь вводит с клавиатуры строку, слово для
#поиска, слово для замены. Произведите в строке замену
#одного слова на другое. Полученную строку отобразите
#на экране.
s = 'hello fd45 hgfhg 65 bv hello 4323vgdbg hello'
word_old = 'hello' #input()
word_new = 'python' #input()
s2 = '' #строка для нового содержимого
left_index = 0 # индекс левого края слова
right_index = 0# индекс правого края слова
for i in range(len(s)): # перебор символов
  if s[i] == ' ' or i == len(s) - 1: # если пробел
    left_index = right_index # сдвиг индексов слова
    right_index = i
    if s[left_index:right_index + 1].lstrip().rstrip() == word_old: # если слово для замены
        s2 += ' ' + word_new # новое слово
    else: # иначе
        s2 += s[left_index:right_index + 1].rstrip() # старое слово
s = s2.lstrip()
print(s)

"""## "Сырые" строки"""

print('Hello \n,World')
print(r'Hello {2 * 2 } \n,World')
print(rf'Hello {2 * 2 } \n,World')

"""## Форматирование вывода"""

login = 'SuperUser'
age = 13
print('Привет', login,'! Я знаю, что ', age,'тебе лет.')
print('Привет, {}! Я знаю, что {} тебе лет'.format( 13, 12, login))
print('Привет, {login}! Я знаю, что {age} тебе лет'.format(age = age, login = login))

"""## Форматная строка"""

login = 'SuperUser'
age = 13
print(f'Привет, {login}! Я знаю, что {age} тебе лет', f'{2**5}')

"""## Модуль String"""

import string
print(string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase)
# string.ascii_lowercase
# string.ascii_uppercase
print(string.digits, string.hexdigits, string.octdigits)
#string.hexdigits
#string.octdigits
print(len(string.punctuation))

# как получить алфавит кириллицы
for i in range(ord('А'), ord('А') + 32):
  print(chr(i), i)

# Генератор паролей
# длина пароля, выбор со знаками пунктуации или без
import string
import random
print('Генератор паролей')
len_password = int(input('Ведите длину пароля'))
choise = input('Использовать спецсимволы\n0-нет\n1-да')
password = ''
if choise == '0':
    char = (string.ascii_letters + string.digits)
    end = 62
else:
    char = (string.ascii_letters + string.digits + string.punctuation)
    end = 94
for i in range(len_password):
    password += char[random.randint(0,end)]
print(password)

"""## Регулярные выражения


***Изменяемость*** — над коллекцией допустимы операции
добавления новых и удаления существующих значений.


***Упорядоченность*** — каждый элемент коллекции характеризуется не только своим значением, но и индексом
(порядковым номером элемента в коллекции). С понятиями
индекса, индексацией и срезами мы уже познакомились
ранее при работе со строками.

***Уникальность*** — коллекция состоит из неуникальных (повторяющихся) элементов.
"""

s = 'fdfd'

listt = ['s',s,23, 43.9, 43, [21, 21]]
print(listt)
listt[0] = 43
print(listt[0], listt[:], listt[-1])