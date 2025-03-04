
"""# Циклы"""

# while цикл с условие
n = 0
while n < 5:
  n += 1
  print(n)
print('end')

n = 2000
while True:
    n -= 1
    if n < 1:
        break
    print('Hello', 200/n)
print('end')

n = 0
while n < 10:
    n += 1
    print(n)
else:
    print('end')

#break
n = 0
while n < 10:
    n += 1
    if n == 8:
        break
    print(n)
else: # выполняется только в случае полного выполнения цикла
    print('end')

# for цикл - счетчик range(start, end, step)
for i in range(11):
  print(i)
  if i == 5: # изменение итерационной переменной
    break
else:# выполняется только в случае полного выполнения цикла
  print('end')

word = 'Hello, Python!'
for i in range(11, 0, -1): # отсчет от большего к меньшему
  print(word[i], word[i+ 1])

name = 'Joe'
for i in 'name':
  print(i)

#continue
a = 0
while a < 10:
  a += 1
  if a % 2 == 1:
    print('нечетное')
  else:
    continue
    print('четное')

"""# Исключения"""

while True:
  try:
    value = int(input('введите количество деталей'))
    box = int(input('введите количество коробок'))
    print(value/box)
  except:
    print('Ошибка!')

#пример иерархии
while True:
  try:
    value = int(input('введите количество деталей'))
    box = int(input('введите количество коробок'))
    print(value/box)
  except Exception:
    print('Введены неверные данные')
  except ZeroDivisionError:
    print('Нельзя разложить в 0 коробок!')

#пример вызова ошибки
while True:
  try:
    value = int(input('введите количество деталей'))
    box = int(input('введите количество коробок'))
    if value/box < 1:
        raise Exception
    print(value/box)
  except ZeroDivisionError:
    print('Нельзя разложить в 0 коробок!')
  except ValueError:
    print('Введены неверные данные!')
  except Exception:
    print('Ошибка счета')

#пример finally
while True:
  try:
    value = int(input('введите количество деталей'))
    box = int(input('введите количество коробок'))
    if value/box < 1:
        raise Exception
    print(value/box)
  except ZeroDivisionError:
    print('Нельзя разложить в 0 коробок!')
  except ValueError:
    print('Введены неверные данные!')
  except Exception:
    print('Ошибка счета')
  finally:
    print('Операция завершена')

#пример просмотра объекта
while True:
  try:
    value = int(input('введите количество деталей'))
    box = int(input('введите количество коробок'))
    if value/box < 1:
        raise Exception
    print(value/box)
  except (ZeroDivisionError):
    print('Нельзя разложить в 0 коробок!')
  #except ValueError:
  #  print('Введены неверные данные!')
  except Exception as ex:
    print('Ошибка счета', type(ex), ex)
  finally:
    print('Операция завершена')
