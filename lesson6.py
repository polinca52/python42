# Сортировка и поиск

##Сортировка пузырьком
"""

# пузырьковая сортировка
array = [4, 12, 7, 2, 10, 5]
for i in range(len(array)):
    for y in range(len(array)):
        if array[i] < array[y]:
            array[i], array[y] = array[y], array[i]
            print(array)

"""## Сортировка вставкой"""

# сортировка методом вставок
for i in range(1, len(array)):
    for y in range(i, 0, -1):
        if array[y] > array[y - 1]:
            array[y], array[y - 1] = array[y - 1], array[y]
            print(array)

"""## Задача"""

#Есть список целых. Необходимо первую половину
#списка отсортировать по убыванию, вторую половину
#по возрастанию.
for i in range(len(array)//2):
    for y in range(len(array)//2):
        if array[i] > array[y]:
            array[i], array[y] = array[y], array[i]
for i in range(len(array)//2, len(array)):
    for y in range(i, len(array)//2, -1):
        if array[y] < array[y - 1]:
            array[y], array[y - 1] = array[y - 1], array[y]
print(array)

# сортировать числа по возрастанию. Сначала идут числа заканчивающиеся 1, потом 2 и т.д.
for i in range(1, len(array)):
    for y in range(i, 0, -1):
        if array[y] % 10 < array[y - 1] % 10:
            array[y], array[y - 1] = array[y - 1], array[y]
        elif array[y] < array[y - 1] and array[y] % 10 == array[y - 1] % 10:
            array[y], array[y - 1] = array[y - 1], array[y]
print(array)

"""## Метод сортировки слияния"""

#метод сортировки слиянием
def split_array(array): # функция деления списка на элементарные части
    l1 = array[:len(array) // 2] #левое число
    l2 = array[len(array) // 2:] #правое число
    if len(l1) > 1: # делим пока в списке останется одно число
        l1 = split_array(l1)
    if len(l2) > 1: # делим пока в списке останется одно число
        l2 = split_array(l2)
    return sorted_merge(l1, l2) # отправляем числа на сравнение(сортировку) и слияние

def sorted_merge(l1, l2): # функция сортировки и слияния
    result_list = [] # итоговый список с сортировкой
    i = 0 #индекс левого подсписка
    y = 0 #индекс правого подсписка
    while i < len(l1) and y < len(l2): # пока индекс есть в одном из подсписков
        if l1[i] < l2[y]: # условие если i-ый элемент левого подсписка меньше y-го правого
            result_list.append(l1[i]) #i-ый элемент левого подсписка
            i += 1 # сдвигается индексация правого подсписка
        else:# иначе то же для левого
            result_list.append(l2[y])
            y += 1
    result_list += l1[i:] + l2[y:] # добавляется четвертое (максимальное оставшееся) в резалт
    return result_list
print(array)
print(split_array(array))

"""## сортировка Шелла"""

# сортировка Шелла
array = [4, 12, 7, 2, 10, 5, 8]
def shell(sort_list):
    len_l = len(sort_list)
    mid = len_l // 2
    while mid > 0:
        for elem in range(mid, len_l):
            current_elem = sort_list[elem]
            indx = elem
            while indx >= mid and sort_list[indx - mid] < current_elem:
                sort_list[indx] = sort_list[indx - mid]
                indx -= mid
                sort_list[indx] = current_elem
        mid //= 2
    return sort_list

"""##Cортировка пирамидальная"""

# пирамидальная сортировка
array = [4, 12, 7, 2, 10, 5, 8]
def b_tree(array, upper, i):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper: #1
            if array[i] >= max(array[l], array[r]):
                break
            elif array[l] > array[r]:
                swap(i, l) #array[i], array[l] = array[l], array[i]
                i = l
            elif array[l] < array[r]:
                swap(i, r) #array[i], array[r] = array[r], array[i]
                i = r
        elif l < upper:
            if array[l] > array[i]:
                swap(i , l)
                i = l
            else:
                break
        elif r < upper:
            if array[r] > array[i]:
                swap(i , r)
                i = r
            else:
                break
        break

def swap(i , child):
    array[i], array[child] = array[child], array[i]

def heap_sort(array):
    for y in range((len(array) - 2)//2, -1, -1):
        b_tree(array, len(array), y)
    for w in range((len(array) - 1), 0, -1):
        swap(w, 0)
        b_tree(array, w, 0)
    return array

heap_sort(array)
print(heap_sort(array))

"""## быстрая **сортировка**"""

#быстрая сортировка
from random import randint
array = [4, 12, 7, 2, 10, 5, 8]
def quik_sort(array):
    if len(array) > 1:
        n = array[randint(0, len(array) - 1)]
        list_min = [elem for elem in array if elem < n]
        list_equil = [elem for elem in array if elem == n]
        list_max = [elem for elem in array if elem > n]
        list_result = quik_sort(list_max) + quik_sort(list_equil) + quik_sort(list_min)
    else:
        list_result = array
    return list_result
print(quik_sort(array))

"""Есть стопка оладий различного радиуса. Единственная
операция, проводимая с ними — между любыми двумя
суем лопатку и меняем порядок оладий над лопаткой
на обратный. Необходимо за минимальное количество
операций таких отсортировать снизу вверх по убыванию
радиуса
"""

#from random import randint

array = [randint(1,100) for i in range(10)]
print(array)
def check_sort(list):
    for i in range(len(list) - 1):
        if list[i] >= list[i + 1]:
            pass
        else:
            return False
    return True

def search_max(list):
    maxx = 0
    for i in list:
        if i > maxx:
            maxx = i
    return maxx

def rotate(list):
    return list[::-1]
index_sorted = 0
while check_sort(array) == False:
    maxx = search_max(array[index_sorted:])
    array =  array[:array.index(maxx)] + rotate(array[array.index(maxx):])
    array = array[:index_sorted] + rotate(array[index_sorted:])
    index_sorted += 1
    print(index_sorted, array)
print(array)

"""## Линейный поиск"""

#линейный
from random import randint
count = 0
index_list = []
array = [randint(1,5) for i in range(10)]
print(array)
num = int(input('Введи число'))
for i in range(len(array)):
    if array[i] == num:
        count += 1
        index_list.append(i)
if count > 0:
    print(f'найденных чисел {count} шт,индекс: {index_list} ')
else:
    print('Таких чисел нет')

"""## Бинарный поиск"""



"""# Кортеж tuple"""

my_list = [23, 23.45, "23", True, [23, 23]]
print(my_list)
my_list[0] = 32
print(my_list)
# создание кортежа
my_list = tuple(my_list)
print(my_list)
my_tuple = (23, 43, 65)
print(my_tuple)
# изменение кортежа
my_list[4][0] = 32
print(type(my_list))
# одноэлементный кортеж
singl_elem = (3, )
print(type(singl_elem))
# распаковка
*elem1, elem2 = my_tuple
#elem1, *elem2 = my_tuple
print(elem1, elem2)
#конкантенация объединение и повторение
result = my_list + my_tuple
result2 = my_list * 3
print(result, result2)

# преобразование в список
print(result, list(result))

#Пользователь вводит с клавиатуры название фрукта.
#Необходимо вывести на экран количество раз, сколько
#фрукт встречается в кортеже в качестве элемента.
fruit_tuple = ('apple', 'mango', 'banana', 'lemon', 'avocado', 'mango', 'banana', )
fruit = input('введите название фрукта')
cnt = 0
for f in fruit_tuple:
    if f == fruit:
        cnt += 1
print(cnt)

#Добавьте к заданию 1 подсчет количества раз, когда
#название фрукта является частью элемента. Например:
#banana, apple, bananamango, mango, strawberry-banana.
#В примере выше banana встречается три раза.
fruit_tuple = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
fruit = 'banana' #input('введите название')
cnt = 0
for f in fruit_tuple:
    if fruit in f:
        cnt += 1
print(cnt)

#Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0
#до N раз). Пользователь вводит с клавиатуры название
#производителя и слово для замены. Необходимо заменить
#в кортеже все элементы с этим названием на слово для
#замены. Совпадение по названию должно быть полным.
cars_tuple = ('BMW', 'KIA', 'TESLA', 'AUDI', 'AURUS') * 3
old_car = 'KIA' #input('кого заменить')
new_car = 'LADA' #input('на кого заменить')
def change_car(tuple_, old, new):
    tuple_ = list(tuple_)
    for indx_car in range(len(tuple_)):
        if tuple_[indx_car] == old:
            tuple_[indx_car] = new
    tuple_ = tuple(tuple_)
    return tuple_
print(cars_tuple)
print(change_car(cars_tuple, old_car, new_car))

#Есть кортеж с целыми числами. Нужно вывести статистику по
#количеству цифр в элементах кортежа. Например:
#■ 1 цифра — 3 элемента;
#■ 2 цифры — 4 элемента;
#■ 3 цифры — 5 элементов.
tuple_ = (23, 345, 24324, 54, 5424, 432, 53424543, 567)
lenght_list = []
count_list = []
list_ = list(tuple_)
dotn = 1
#print('начало while')
while list_ != []:
    for digit in list_:
        if len(str(digit)) == dotn:
            count_list.append(dotn)
            if dotn not in lenght_list:
                lenght_list.append(dotn)
            list_.remove(digit)
            print(list_)
        if len(list_) == 1:
            if len(str(list_[0])) == dotn:
                count_list.append(dotn)
                if dotn not in lenght_list:
                    lenght_list.append(dotn)
                list_ = []
    dotn += 1
    print(list_, dotn)
#print('конец w')
for i in lenght_list:
    print(f'{i} значных чисел {count_list.count(i)} шт')

"""## ## Множество"""

my_list = [True, False, True, 'True', 1]
print(my_list) # список
my_list = set(my_list)
print(my_list)# множество
# индексация
#print(my_list[0])
#for i in range(1000):
#    for y in my_list:
#        print(y, end='')
#    print()
#добавление и удаление
my_list.add(34)
my_list.remove('True')
for i in range(1000):
    for y in my_list:
        print(y, end='')
    print()
#объединение
my_set = {23, 32, 34, 1}
print(my_list & my_set)
print(my_list | my_set)
print(my_list ^ my_set)

"""##Cловари"""

#Словари
#cоздание словаря
my_dict = {'name': 'Joe', 'age':67, 'weight': 67, 0 : 0}
print(my_dict)
print(my_dict['name']) # получение value по key
print(my_dict.keys()) # получение списка ключей key
print(my_dict.values()) # получение списка значений values
print(my_dict.items()) # получение пары ключей key и  значений values
color_dict = {'red':'красный', 'green': 'зеленый', 'grey':'серый', 'black':'черный' }
print('red' in color_dict)
print('красный' in color_dict)
# методы возрата значений
print(color_dict.get('red', 'КЛЮЧА НЕТ')) # возвращает значение по ключу
print(color_dict)
print(color_dict.setdefault('white', 'КЛЮЧА НЕТ')) #возвращает значение по ключу, а при отсутствии добавляет ключ со значением
print(color_dict)
#изменение  словаря
color_dict.update(my_dict) # объединение словарей
color_dict['white'] = 'белый' # добавление по ключу key
del(color_dict['age']) # удаление по ключу key
clone_dict = color_dict.copy() # копирование словаря
color_dict['yellow'] = 'жёлтый'
print(color_dict, clone_dict)