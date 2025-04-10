#class Node:
#    def __init__(self, name, next_node = None, prev_node = None):
#        self.name = name
#        self.next_node = next_node
#        self.prev_node = prev_node
#class Queue:
#    length = 0
#    max_length = 4
#    head = None
#    tail = None
#
#
#
#    def IsEmpty(self):                  
#        if self.length == 0:
#            print('очередь пуста')
#            return True
#        else:
#            print('очередь не пуста')
#            return False
#        
#
#    def Enqueue(self,name):                  # добавление элемента в очередь.
#        if self.length < self.max_length:
#            if self.head == None:
#                self.head = self.tail= Node(name)
#            else:
#                new_node = Node(name, prev_node = self.tail)
#                self.tail.next_node = new_node
#                self.tail = new_node
#            self.length +=1
#        else:
#            print( f'очередь заполнена')
#
#
#    def Show(self):                 # отображение всех элементов очереди на экран.
#        try:
#            num_in_queue = 1
#            line = f'очередь: '
#            current_node = self.head
#            while current_node.next_node != None:
#                line += f'{num_in_queue}-{current_node.name}, '
#                num_in_queue += 1
#                current_node = current_node.next_node
#            line += f'{num_in_queue}-{current_node.name}.'
#            return line
#        except:
#            return f'очередь пуста'
#    def Dequeue(self):                       #удаление элемента из очереди.
#        try:
#            if self.head.next_node is None:
#                del self.head
#            else:
#                self.head = self.head.next_node 
#                del self.head.prev_node
#            self.length -= 1
#        except:
#            print('удалять не кого')
#    
#    def IsFull(self):
#        if self.length == self.max_length:
#            print('очередь заполнена')
#            return True
#        else:
#            print('очередь не заполнина')
#            return False
#
#queue_in_market = Queue()
#queue_in_market.Enqueue('denis1')
#queue_in_market.Enqueue('denis2')
#queue_in_market.Enqueue('denis3')
#queue_in_market.Enqueue('denis4')
#queue_in_market.Dequeue()
#queue_in_market.Dequeue()
#queue_in_market.Dequeue()
#queue_in_market.Dequeue()
#queue_in_market.Dequeue()
#
#
#print(queue_in_market.Show())

#2
class Node:
    def __init__(self,task, priority, next_node = None, prev_node = None):
        self.task = task
        self.priority = abs(float(priority))
        self.next_node = next_node
        self.prev_node = prev_node

class PriorityQueue:
    head = None
    length = 0
    max_length = 4

    def show(self):
        if self.head is None:
            print('очередь пуста')
        else:
            line = f'Очередь: \n'
            current_node = self.head
            while current_node.next_node != None:
                line += f'#{current_node.priority}# {current_node.task}'
                current_node = current_node.next_node
            line += f'#{current_node.priority}# {current_node.task}'
            print(line)
            return line
            
    def insert_with_priority(self, task, priority):
        #new_node = Node()
        if self.head is None:
            self.head = Node(task, priority)
            self.length += 1
        elif self.length < self.max_length:
            current_node = self.head
            if priority < current_node.priority:
                current_node.prev_node = Node(task, priority,next_node=current_node)
                self.head = current_node.prev_node
                self.length += 1
                return f'элемент добавлен'
            while current_node.next_node != None:
                if current_node.priority > priority:
                    #current_node.prev_node = Node(task, priority, next_node=current_node, prev_node=current_node)
                    #current_node.prev_node = current_node.prev_node.next_node
                    new_node = Node(task, priority, next_node=current_node, prev_node=current_node.prev_node)
                    current_node.prev_node.next_node = new_node
                    current_node.prev_node = new_node
                    self.length += 1
                    return f'элемент добавлен'
                else:
                    current_node = current_node.next_node

            if priority < current_node.priority:
                current_node.prev_node.next_node =   current_node.prev_node = Node(task, priority,next_node=current_node, prev_node = current_node.prev_node)
            else:
                current_node.next_node = Node(task, priority, prev_node=current_node)
          
            #добавить связь с предидущем

            self.length += 1
            return f'элемент добавлен'
        else:
            return f'добавление не возможно очередь заполнена'
        
    
    def pull_highest_priority_element(self):
        try:
            if self.length > 1:
                self.head = self.head.next_node
                del self.head.prev_node
            else:
                del self.head
            self.length -= 1
        except:
            print('очередь пуста', self.length)
    
    def peek(self):
        if self.length != 0:
            print(f'#{self.head.priority}# {self.head.task}')
            return f'#{self.head.priority}# {self.head.task}'
        else:
            print('очередь пуста')

tobo = PriorityQueue()

tobo.insert_with_priority('задание 1', 2)
tobo.insert_with_priority('задание 2', -1)
tobo.insert_with_priority('задание 3', 1.2)
tobo.insert_with_priority('задание 4', 5)
tobo.insert_with_priority('задание 5', 2.2)
tobo.pull_highest_priority_element()
tobo.pull_highest_priority_element()

tobo.peek()
#tobo.show()                    