##упаковка (щператор *)
#var1 = 34
#var2 = 'Python'
#var3 = True
#*my_list, = var1, var2, var3
#print(my_list)
#
##распаковка
#list= [34, 'helloy', False] * 2
##a, b, c = list
##a, *b = list
#c, *a, b = list
#print(a,b)
#
#def f(*args):
#    print(args)
#
#f(23,45,7,2,87,45,23,87,56,5)
#
##рыспаковка **
#
#def f(**kwargs):
#    print(kwargs)
#
#f(param1=34,param2 = 'dog', param3 = True)
#f(age = 34, nick = 'pop', param3 = True)
#
##заспаковка в цепи
#list_users = [
#    ['Micky', 'Mouse'],
#    ['Vladimir','Putin'],
#    ['pop','top']
#]
#
##for name, last_name in list_users:
##    print(f'Name:{ name}; last name: {last_name}\n')
##line = -7, 10
##print(line)
##for i in range(*line):
##    print (i)
#
#print(*range(10))

#Есть некоторый словарь, который хранит названия
#стран и столиц. Название страны используется в качестве
#ключа, название столицыв качестве значения. Необходимо
#реализовать: добавление данных, удаление данных, поиск
#данных, редактирование данных, сохранение и загрузку
#данных (используя упаковку и распаковку).

def add_data(country_dict):
    data = input('введите страну и столицу через пробел')
    country, capital = data.split(' ')
    if country in country_dict.keys():
        print('чувак такая страна есть')
    else:
        country_dict[country] = capital
    return country_dict

def delete_date(country_dict):
    data = input('введите страну для удаления')
    if data in country_dict.keys():
        del country_dict[data]
        print(f'cстрана {data} удалена')
    else:
        print('чувак такой странны нет')
    return country_dict

def searche_data(country_dict):
    data = input('введите страну или столицу дл япоиска')
    for country, capital in country_dict.items():
        if data == country or data == capital:
            print(f'результат поиска: \n {country} {capital}')
            break
    else:
        print('нет')
    return country_dict

def update_data(country_dict):
    data = input('введите страну и новую столицу ')
    country, capital = data.split(' ')
    country_dict[country] = capital
    return country_dict

def save_data(country_dict):
    data = ''
    for key, value in country_dict.items():
        data += f'{key}:{value}\n'
    with open('country_dict.txt', 'w') as file:
        file.write(data) 
    return country_dict      

def load_data(country_dict):
    with open('country_dict.txt', 'r') as file:
        for line in file:
            country, capital = line.split(':')
            country_dict[country] = capital
    return country_dict



    


country_dict ={}
while True:
    print(country_dict)
    choice = int(input('База стран и столиц\nменю:\n1-Добавить\n2-удалить\n3-поиск\n4-редоктирование\n5-сохранение\n6-загрузка\n0 - выход'))
    if choice == 0:
        break
    elif choice == 1:
         add_data(country_dict)
    elif choice == 2:
        delete_date(country_dict)
    elif choice == 3:
        searche_data(country_dict)
    elif choice == 4:
        update_data(country_dict)
    elif choice == 5:
        save_data(country_dict)
    elif choice == 6:
        load_data(country_dict)

        


