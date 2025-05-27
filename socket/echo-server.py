import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:   #созданние сокета с протоколом и типом подключения 
    host = '127.0.0.1'
    port = 5000
    s.bind((host,port))  #связывание с адресом
    print(f'server{host} runer')
    s.listen() #прослушивание и установление соединения
    conn, addres = s.accept() #клиент инициирует соединение с сервером
    while True:
        date = conn.recv(1024)
        if date == False:
            break
        conn.sendall(date)