#class Node:
#    def __init__(self, value, next_node = None, prev_node = None):
#        self.value = value
#        self.next_node = next_node
#        self.prev_node = prev_node
#        
#
#class DoubleLinkList:
#    head = None
#    tail = None
#    lenght = 0
#    #методы
#    def my_append(self,value):
#        if  self.head == None:
#            self.head = Node(value)
#            self.tail = self.head
#        else:
#            #currend_node = self.head
#            #while currend_node != None:
#            #    currend_node = currend_node.naxt_node
#            #    currend_node.naxt_node = Node(value, prev_node = currend_node)
#            #self.tail = currend_node.next_node 
#            currend_node = self.tail
#            currend_node.next_node = Node(value, prev_node = currend_node)
#            self.tail = currend_node.next_node
#        self.lenght += 1
#    def __str__(self):
#        line = '<<' 
#        currend_node = self.head
#        while currend_node.next_node != None:
#            line += f'{currend_node.value}, '
#            currend_node = currend_node.next_node
#        line += f"{currend_node.value} >>"                                                                                                                                                                                                                                                                                                                                                  
#        return line
#
#double_link_list = DoubleLinkList()
#double_link_list.my_append(52)
#double_link_list.my_append(52)
#double_link_list.my_append(-5)
#
#print(double_link_list)

#task1
#class Node:
#    def __init__(self, value, next_node = None, prev_node = None):
#        self.value = value
#        self.next_node = next_node
#        self.prev_node = prev_node
#        
#
#class DoubleLinkList:
#    head = None
#    tail = None
#    lenght = 0
#    #методы
#    def my_append(self,value):
#        if  self.head == None:
#            self.head = Node(value)
#            self.tail = self.head
#        else:
#            #currend_node = self.head
#            #while currend_node != None:
#            #    currend_node = currend_node.naxt_node
#            #    currend_node.naxt_node = Node(value, prev_node = currend_node)
#            #self.tail = currend_node.next_node 
#            currend_node = self.tail
#            currend_node.next_node = Node(value, prev_node = currend_node)
#            self.tail = currend_node.next_node
#        self.lenght += 1
#    def __str__(self):
#        line = '<<' 
#        currend_node = self.head
#        while currend_node.next_node != None:
#            line += f'{currend_node.value}, '
#            currend_node = currend_node.next_node
#        line += f"{currend_node.value} >>"                                                                                                                                                                                                                                                                                                                                                  
#        return line
#    
#    def get_value(self, value_from_searh): #проверить есть ли в списке
#        currend_node = self.head
#        while currend_node.next_node != None:
#            if currend_node.value == value_from_searh:
#                return True
#            currend_node = currend_node.next_node
#        if currend_node.value == value_from_searh:
#                return True
#        else:
#            return False
#    def del_value(self, value_from_delete): #удаление
#        if self.head.value == value_from_delete:#удаление головы
#            node_from_delete = self.head
#            self.head = self.head.next_node
#            self.head.prev_node = None
#            del node_from_delete
#        elif self.tail.value == value_from_delete: #удаление хвоста
#            node_from_delete = self.tail
#            self.tail = self.tail.prev_node
#            self.tail.next_node = None
#        else:                                    #удаление между головой и хвостом
#            currend_node = self.head
#            while currend_node.next_node != None:
#                if currend_node.value == value_from_delete:
#                    node_from_delete = currend_node
#                    currend_node.prev_node.next_node = currend_node.next_node
#                    currend_node.prev_node.prev_node = currend_node.prev_node
#                currend_node = currend_node.next_node
#        del node_from_delete
#        self.lenght -= 1
#
#    def update_value(self,old_value, value_from_update):     #замена 
#        currend_node = self.head
#        while currend_node.next_node != None:
#            if currend_node.value == old_value:
#                currend_node.value = value_from_update
#            currend_node = currend_node.next_node
#        if currend_node.value == old_value:
#            currend_node.value = value_from_update
#
#
#
#double_link_list = DoubleLinkList()
#double_link_list.my_append(52)
#double_link_list.my_append(50)
#double_link_list.my_append(32)
#double_link_list.my_append(15)
#double_link_list.my_append(-5)
#double_link_list.update_value(32, 100)
#
#print(double_link_list)

#task3
class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class Stack:
    head = None
    tail = None
    length = 0
    max_length = 4

    def stack_append(self,value):             #проверка на заполненность стека и помещение в стейк
        if self.length < self.max_length:
            if  self.head == None:
                self.head = Node(value)
                self.tail = self.head
            else:                                      
                currend_node = self.tail
                currend_node.next_node = Node(value, prev_node = currend_node)
                self.tail = currend_node.next_node
            self.length += 1
        else:
            print('стак заполнен')
    
    def stack_pop(self): #удаление хвоста
        node_from_delete = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        self.length -= 1
        del node_from_delete
    
    def get_length(self):         #кол-во элементов
        print(f'в стейке {self.length} элементов')

    def check_empty(self):       #проверка на заполненность 
        if self.head is None:
            print('стейк пуст')
        else:
            print('стэк не пуст')
    
    def stack_clear(self):                 # очистка стека
        currend_node = self.head
        while currend_node.next_node != None:
            node_from_delete = currend_node
            currend_node = currend_node.next_node
            del node_from_delete
        del currend_node
        self.length = 0
        self.head = None
        self.tail = None
    def get_tail(self):
        print(f'последний элемент{self.tail.value}')


    
    
my_stack = Stack()

#double_link_list.stack_append(52)
#double_link_list.stack_append(50)
#double_link_list.stack_append(32)
#double_link_list.stack_append(15)
#double_link_list.stack_append(-5)
##double_link_list.stack_pop()
#double_link_list.get_length()
#double_link_list.check_empty()
#double_link_list.stack_pop()
#
##double_link_list.stack_clear()
#double_link_list.get_length()
#double_link_list.get_tail()

array= input('Введите числа через поробел')
array = array.split(' ')
for elem in array:
    my_stack.stack_append(elem)

while True:
    choice = input(f'1-добавить\n2-удалить\n3-вывод помледнего\n4-проверка пустого\n5-очистить\n0-выход')
    if choice == '1':
        value = input('введите значение для добовления')
        my_stack.stack_append(value)
    elif choice == '2':
        my_stack.stack_pop()
    elif choice == '3':
        my_stack.get_tail()
    elif choice == '4':
        my_stack.check_empty()
    elif choice == '5':
        my_stack.stack_clear()
    elif choice == '0':
        break
print('программа завершина')

        

