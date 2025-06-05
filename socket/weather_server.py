#Реализуйте погодное клиент-серверное приложение.
#Клиент обращается к серверу с указанием: страны и города. Сервер, получив запрос, возвращает погоду на неделю
#для данной местности. Используйте для реализации приложения механизмы многопоточности. Данные о погоде
#должны быть предопределенными и взяты из файла.

import socket
import threading
def load_weather(path, city):
    with open(path,'r',encoding='utf-8') as file:
        for item in file:
            if item.split(';')[0] == city:
                return item.split(';')[1:]
        else:
            return False

def handle_client(conn, address):
    path = 'C:/Project42/socket/weather.txt'
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    message = 'Weather:\n'
    print(f'Connect client {address}')
    conn.sendall('Hello!'.encode())
    while True:
        city = conn.recv(1024).decode(encoding='utf-8')
        if city == False:
            print('Disconnect')
            break
        date = load_weather(path, city)
        if date == False:
            message = 'City not found'
        for day in range(7):
            message += f'{week[day]} : {date[day]}\n'
        conn.sendall(message.encode())

host = '127.0.0.1'
port = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    print(f'server {host} runer')
    s.listen(5)
    while True:
        conn, address = s.accept()
        threading.Thread(name='1', target=handle_client, args=(conn, address)).start()

