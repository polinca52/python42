import socket

def handle_client(conn,adderson ):
    print(f'connect clinet {adderson}')
    conn.sendall('Hellou'.encode())
    while True:
        date=conn.recv(1024).decode(encoding = 'utf-8')
        if date == False:
            print('Disconect')
            break
        print(f'massag from {addres}: {date}')
        response = input('inpunt response to client')
        conn.sendall((response + '\n').encode())

host = '127.0.0.1'
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    
    s.bind((host,port))
    print(f'server{host} runer')
    s.listen()
    while True:
        conn, addres = s.accept()
        handle_client(conn,addres)
        print('ожидайте следуйщего')