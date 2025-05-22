#import threading
##def f(a,b):
##    print(a+b)
##    return a + b
##
##def s(a=0):
##    print(a**2)
##    return a**2
##thread_1 = threading.Thread(name = 'поток первый', target=f, args=(10, 15))  # перердача аргементов функции котеджом
##thread_2 = threading.Thread(name = 'поток второй', target=s, kwargs={'a':3})   # перердача аргементов функции словарем
##thread_2.start()
##thread_1.start()
##print(thread_1)
#import time
#
#def counter(t):
#    while t < 10:
#        print(t)
#        time.sleep(t)
#        t+=2
#
#def welcom(name = 'None'):
#    while True:
#        print('welcom, ', name)
#        time.sleep(2)
#
#thread_counter = threading.Thread(name='thread counter', target=counter, args={0,})
#thread_welcom = threading.Thread(name='thread welcom', target=welcom, kwargs={'name':'ivan'})
#
#print('начало программы')
#thread_counter.start()
#print('середина программы')
#thread_welcom.start()
#thread_counter.join()
#print('конец программы')

#Task1
#Пользователь с клавиатуры вводит значения в список.
#После чего запускаются две потока. Первый поток находит максимум в списке. Второй поток находит минимум
#в списке. Результаты вычислений выводятся на экран.
#import threading
#var1
#def max_num(list=0):
#    print('max значение', max(list)) 
#
#def min_num(list=0):
#    print('min значение', min(list)) 
#var2
#def stat_num(list=0, mode = 'max'):
#    if mode != 'max':
#        print('', max(list))
#    else:
#        print('', min(list))
#    
#
#num = int(input('введите число: '))
#list_=[]
#while num != 0:
#    list_.append(num)
#    num = int(input('введите число: '))
#
#thread_max = threading.Thread(name='thread max', target=stat_num, kwargs={'list':list_,'mode':'max'})
#thread_min = threading.Thread(name='thread min', target=stat_num, kwargs={'list':list_,'mode':'min'})
#thread_max.start()
#thread_min.start()

#Task2
#import threading
#def summ(list=0):
#    print(sum(list))
#
#def aver(list = 0):
#    print(sum(list)/len(list)) 
#
#
#num = int(input('введите число: '))
#list_=[]
#while num != 0:
#    list_.append(num)
#    num = int(input('введите число: '))
#
#t1 = threading.Thread(name = 'summa', target= summ, kwargs={'list':list_})
#t2 = threading.Thread(name='aver',target=aver, kwargs={'list':list_} )
#t1.start()
#t2.start()

#Task3
import threading
path = 'C:\\python42\\Thread\\num.txt'
def even(path):
    with open(path, 'r') as file:
        with open('C:\\python42\\Thread\\even.txt', 'a') as even:
            for num in file:
                if int(num) % 2 == 0:
                    even.write(num)
                else:
                    with open('C:\\python42\\Thread\\odd.txt', 'a') as odd:
                        odd.write(num)

t = threading.Thread(name='lol', target= even, args=(path,))
t.start()


