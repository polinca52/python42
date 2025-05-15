class Basket:
    def __init__(self):
        self.list_order = []
        self.basket_summa = 0
    
    def add_order(self, pizza):
        self.list_order.append(pizza)
        self.basket_summa += pizza.price
    
    def del_oprder(self, num_order):
        obj_del = self.list_order[num_order-1]
        self.list_order.remove(obj_del)
        self.basket_summa -= obj_del.price
        del obj_del

    def get_summa(self):
        return self.basket_summa
    
    def get_list_order(self):
        line = ''
        for item in range(len(self.list_order)):
            line += f'{item+1}. {self.list_order[item].name}\n'
        return line

class PizzaBase:
    def __init__(self,name,price,topping={}):
        self.name = name
        self.price = price
        self.topping = topping
        if self.topping != False:
            for value in self.topping.values():
                self.price += value
    
    def set_recipe(self, recipe):
        for value in recipe.values():
            self.price += value

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.name

class PizzaMargarita(PizzaBase):
    def __init__(self, name, price, topping={}):
        super().__init__(name, price, topping)
    
    def get_name(self):
        return super().get_name
    
    def get_price(self):
        return super().get_price
    
class PizzaPepperoni(PizzaBase):
    def __init__(self, name, price, topping={}):
        super().__init__(name, price, topping)
    
    def get_name(self):
        return super().get_name
    
    def get_price(self):
        return super().get_price

class PizzaHawaii(PizzaBase):
    def __init__(self, name, price, topping={}):
        super().__init__(name, price, topping)
    
    def get_name(self):
        return super().get_name
    
    def get_price(self):
        return super().get_price

class Topping:
    def __init__(self):
        self.topping = {'лук':30,'сoус':40,'перец':50}
 
    def add_topping(self):
        menu = None
        order_topping = {}
        while menu != '0':
            print(self.topping.keys())
            menu = input('название топиннага, 0- выход ')
            if menu == '0':
                break
            order_topping[menu] = self.topping[menu]
        return order_topping

class Recipe:
    def __init__(self):
        self.recipe = {'колбаса':70, 'сыр': 52, 'оливки':145,'маслины':150,'томаты':35,'огурец':30,'ананас':100}
    
    def create_recipe(self): 
        menu = None
        order_recipe = {}
        while menu != '0':
            print(self.recipe.keys())
            menu = input('название топиннага, 0- выход ')
            if menu == '0':
                break
            order_recipe[menu] = self.recipe[menu]
        return order_recipe    
    
class Controller:
    def __init__(self):
        self.pizza_counter = 0
        self.revennue = 0
        self.profit = self.revennue * 0.2

    def basket_counter(self,basket):
        self.pizza_counter += len(basket.list_order)    
        self.revennue += basket.basket_summa
        self.profit = self.revennue * 0.2
    
    def get_statistic(self):
        return f'кол-во пицц: {self.pizza_counter}, выручка: {self.revennue} rub, прибыль {self.profit} rub'