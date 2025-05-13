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
    def __init__(self,name,price,topping=[]):
        self.name = name
        self.price = price
        self.topping = topping

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.name

class PizzaMargarita(PizzaBase):
    def __init__(self, name, price, topping=[]):
        super().__init__(name, price, topping)
    
    def get_name(self):
        return super().get_name
    
    def get_price(self):
        return super().get_price
    
class PizzaPepperoni(PizzaBase):
    def __init__(self, name, price, topping=[]):
        super().__init__(name, price, topping)
    
    def get_name(self):
        return super().get_name
    
    def get_price(self):
        return super().get_price

class PizzaHawaii(PizzaBase):
    def __init__(self, name, price, topping=[]):
        super().__init__(name, price, topping)
    
    def get_name(self):
        return super().get_name
    
    def get_price(self):
        return super().get_price


