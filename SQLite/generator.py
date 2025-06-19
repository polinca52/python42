from random import choice, randint
def create_student():
    #name
    list_name =[ "Alexei", "Ivan", "Dmitry", "Sergey", "Andrey", "Vladimir", "Mikhail", "Nikolay", "Yuri", "Viktor", "Pavel", "Oleg", "Artem", "Kirill", "Roman", "Egor", "Vasily", "Gennady", "Leonid", "Fedor", "Semyon", "Timur", "Valery", "Yevgeny", "Vladislav", "Gleb", "Ilya"]
    name = choice(list_name)
    #age 
    age = randint(17, 30)
    #city
    list_city = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan", "Chelyabinsk", "Omsk", "Samara", "Rostov-on-Don", "Ufa", "Krasnoyarsk", "Perm", "Voronezh", "Volgograd", "Krasnodar", "Saratov", "Tolyatti", "Tyumen", "Izhevsk", "Barnaul", "Ulyanovsk", "Irkutsk", "Khabarovsk", "Yaroslavl", "Vladivostok", "Makhachkala", "Tomsk"]
    city = choice(list_city)
    #country
    list_country = ['Russia','Belorussia','Kazahstan','China']
    counntry = choice(list_country)
    #mail
    mail =name.lower()+str(age)+'@mail.ru'
    #phone
    phone = '+7'+ str(randint(1000000000, 9999999999))
    #group
    list_group = ['web', 'designe', 'test', 'python', 'SMM','бездари'] 
    group = choice(list_group)
    #aver_value
    aver_value = randint(20, 50)/10
    #min_theme
    list_theme = ['web designe', 'computer_science', 'coging', 'math', 'english', 'startup']
    min_theme = choice(list_theme)
    #max_theme
    max_theme = choice(list_theme)
    return name, age, city, counntry, mail, phone, group, aver_value, min_theme, max_theme

def create_departament():
    list = []
    for i in range(1,6):        
        building = i
        name = ['Хирургия', 'Психиатор', 'Морг', 'Педиатрия', 'админка', 'тех.поддержка'][i-1]
        list.append([building, name])
    return list

def create_doctors():
    list_name =[ "Alexei", "Ivan", "Dmitry", "Sergey", "Andrey", "Vladimir", "Mikhail", "Nikolay", "Yuri", "Viktor", "Pavel", "Oleg", "Artem", "Kirill", "Roman", "Egor", "Vasily", "Gennady", "Leonid", "Fedor", "Semyon", "Timur", "Valery", "Yevgeny", "Vladislav", "Gleb", "Ilya"]
    name = choice(list_name)
    phone = '+7'+ str(randint(1000000000, 9999999999))
    salary = randint(17_500, 300_500)
    return name, phone,salary

def create_wards():
    list = []
    for i in range(1,6):
        buildig = i
        for y in range(1,10):
            floor =y
            for x in range(10):              
                number = str(floor) + str(x)
                list.append([buildig,floor, int(number)])
    return list

list_deportament = create_departament()

list_doctors = []
for i in range(29):
    list_doctors.append(create_doctors())

list_wards = create_wards()
hospital_info = (list_deportament, list_doctors, list_wards)