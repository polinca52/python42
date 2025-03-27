#Декораторы
#@lru_cache 
#from functools import lru_cache
#
#@lru_cache
#def f(n):
#    if n <= 1: return 1
#    elif n< 1 and n % 2 == 0: return f(n - 1)*n + f(n - 2)*n
#    else: return f(n-1)*n + f(n - 2 )* n 
#
#print(f(9))
#

# def f2(func):
#    print('декорируемое действие')
#    func()
#    print("второе декорируемое действие")
#
#@f2
#def f1():
#    print("какое-то важное действие")
#
#@f2
#def f3():
#    print('мало важная функция')
#
##var = f2(f1)
#var2 = f1
#var3 = f3
#print(var2, var3)


#1
#from datetime import datetime
#
#def render():
#    print('*'*10)
#    print(weekday())
#    timer() #создать функцию
#    print('*'*10)
#def timer():
#    time = datetime.now()
#    time = time.strftime('%H:%M')
#    print(time)
#
#def weekday():
#    today = datetime.today().weekday()
#    week = ['пн',"вт","ср","чт","пт","сб","вс"]
#    return week[today]
#
#render()

#3
#from datetime import datetime
#
#def render(func):
#    print('*'*10)
#    func() #создать функцию
#    print('*'*10)
#
#@render
#def timer():
#    time = datetime.now()
#    time = time.strftime('%H:%M')
#    print(time)
#
#render

#4
margo_recipe = ('маргорита','салат','сыр','томаты', 'лук')
cheese_recipe = ('4сыра','сыр 1', 'сыр 2', 'сыр 3')
hawail_recipe = ('гавайская','ананас','салат','томаты', 'соус','сыр','курица','лук')
kapri_recipe = ('капричоза','соус','моцарелла','ветчина','грибы','артишок','маслины')
recipe_list = (None,margo_recipe,cheese_recipe,hawail_recipe,kapri_recipe)

margo_price =800
cheese_price = 750
hawail_price= 990
kapri_price = 940
price_list = (None,margo_price,cheese_price,hawail_price,kapri_price)
ticket = []
def menu():
    global ticket
    print('добро пожаловать в пиццерию')
    busket = 0
    pizza_name = []
    while True:       
        pizza = int(input('меню:\n1-маргарита\n2-4сыра\n3 -гавайская\n4 -капричева\n0-выход'))
        if pizza == 0: break
        ticket += [recipe_list[pizza]]
        pizza_name += [recipe_list[pizza][0]]
        busket += price_list[pizza]
        print(f'ваш заказ {pizza_name}, на сумму {busket}')
    print(f'ваш заказ {pizza_name}, на сумму {busket}')
    craft

def craft(func):
    print('разогреть печь')
    func(ticket)
    print('достать гоовую пиццу!')

@craft
def recipe(ticket):
    print('подготовить ингридиенты:')
    for pizza in ticket:
        for i in pizza[1:]:
            pizza(i)
        print('выложить ингридиенты на основу пиццы')
        print('добавить соус')
        print('поместите в печь')
    
menu()