from model import Basket, PizzaMargarita,PizzaHawaii,PizzaPepperoni
class Menu:
    def start_menu():
        basket = Basket()
        topping = {'лук':30,'сщус':40,'перец':50}
        while True:
            print('menu:')
            menu = input('1-Создать заказ\n2-статистика')
            if menu == '1':
                menu = input('1-маргарита\n2-пеперони\n3-гавайская\n4-свой рецепт')
                order_topping = {}
                if menu == '1':
                    while menu != '0':
                        print(topping.keys)
                        menu = input('название топиннага, 0- выход ')
                        if menu == '0':
                            break
                        order_topping[menu] = topping[menu]
                    pizza = PizzaMargarita('маргарита', 12000, )
                elif menu == '2':
                elif menu == '3':
                else:

