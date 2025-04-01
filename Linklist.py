##динамический массив
#array = [43, 543,34, 87, 434, 7, 987, 34]
#print(array[3])
#array.append(-1)
#array.insert(3,0)
#array.remove(7)
#array.pop(2)
#print(array)


class Linklist:
    lenght = 0
    head = None
    class Node:
        def __init__(self, value, next_node = None):
            self.value = value
            self.next_node = next_node
    def my_append(self, value):
        if self.head is None:
            self.head = Linklist.Node(value)
        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = Linklist.Node(value)
        self.lenght += 1

    def __str__(self):
        resylt_line = '<$'
        current_node = self.head
        while current_node.next_node != None:
            resylt_line += f" {current_node.value}, "
            current_node = current_node.next_node
        resylt_line += f"{current_node.value} $>"                                                                                                                                                                                                                                                                                                                                                  
        return resylt_line
    
    def search(self, value_from_search):
        current_node = self.head
        while current_node.next_node != None:
            if current_node.value == value_from_search:
                return True
            current_node =current_node.next_node
        if current_node.value == value_from_search:
            return True
        else:
            return False
    def my_remove(self, value_from_remove):
        current_node = self.head
        if self.head.value == value_from_remove:
                self.head = current_node.next_node
                del current_node
                self.lenght -= 1
                return'элемент удален'
        while current_node.next_node != None:
            if current_node.next_node.value == value_from_remove:
                current_node.next_node = current_node.next_node.next_node
                del current_node.next_node
                self.lenght -= 1
                return'элемент удален'
            current_node =current_node.next_node
        return'элемент не найден'
    

    def update(self, old_value, new_value):
        current_node = self.head
        while current_node.next_node != None:
            if current_node.value == old_value:
                current_node.value = new_value
                return 'данные изменины'
            current_node = current_node.next_node
        if current_node.value == old_value:
            current_node.value = new_value
            return 'данные изменины'
        else:
            return 'данные не обнавлены'
            

my_array = Linklist()
my_array.my_append(52)
my_array.my_append(-5)
my_array.my_append(0)
my_array.my_append(5342)
#print(my_array.my_remove())
#print(my_array)

#array= input('Введите числа через поробел')
#link_list = Linklist()
#array =array.split(' ')
#for elem in array:
#    link_list.my_append(elem)
#
#while True:
#    print(f'ваш массив чисел: {link_list}')
#    choice = input(f'1-добавить\n2-удалить\n3-поиск\n4-заменить\n5-вывод\n0-выход')
#    if choice == '1':
#        value = input('введите значение для добовления')
#        link_list.my_append(value)
#    elif choice == '2':
#        value = input('введите значение для удаления')
#        link_list.my_remove(value)
#    elif choice == '3':
#        value = input('введите значение для поиска')
#        print(link_list.search(value))
#    elif choice == '4':
#        old_value = input('введите значение для замены')
#        new_value = input('введите заменяемое число')
#        link_list.update(old_value, new_value)
#    elif choice == '0':
#        break
#print('программа завершина')
#
#        
#
#