#SOLID - паттерн проектиррования согласно принцепам ООП
#     S - единственная ответственность у класса (экземпляр класа0)
#class Loader:
#    def __init__(self,text, path):
#        self.text  = text
#        self.path = path
#    
#    def load(self):
#        with open(self.path, 'w', encoding= 'utf-8') as file:
#            file.write(self.text)
#
#class Uploader:
#    def __init__(self,path):
#        self.text  = ''
#        self.path = path
#    
#    def upload(self):
#       with open(self.path, 'r') as file:
#           self.text = file.read()
#       return self.text
    
#text = 'тун тун сагур'
#path = 'python42/pattern_SOLID/file.txt'
#
#loader = Loader(text,path)
#loader.load()
#       O - открытость 5к расширению, но закрытось к изменнению  
#from pickle import dump
#class Loader:
#    def __init__(self,text, path):
#        self.text  = text
#        self.path = path
#    
#    def load(self):
#        with open(self.path+'.txt', 'w', encoding= 'utf-8') as file:
#            file.write(self.text)
## расширим функционал класса записью в pikle
#    def load_for_pickle(self, object_load):
#         with open(self.path+'.pkl', 'wb') as file:
#              dump(object_load, file)
##но не изменяем фуекцию при необходимости зеализуем его в других классах(объектах)
#class MyClass:
#     def __init__(self):
#          self.arg = 'Test'
#obj = MyClass()
#text = 'тун тун сагур'
#path = 'python42/pattern_SOLID/file.txt'
#loader = Loader(text, path)
#loader.load_for_pickle(obj)
#     L - принцип замещения Барбары Лисков
#Функционалб логика поведения и т.п. должн а легко замещаться
#от супер-класса к суб-классу и наоборот

#     I - разделения интерфейсов (нет неиспользуемых интерфейсов)
# реализация и использование только необходимых и достаточных функций объекта

#     D - инверсия зависимостию Высокоуровневые классы не зависят от низкоуровневых.    

