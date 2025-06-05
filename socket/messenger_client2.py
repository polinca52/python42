import socket
import threading
def incoming():
    while True:
        message = s.recv(1024).decode('utf-8')
        if message == False:
            break
        print('massage:',message)
host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print('welcome to chat')
    
    threading.Thread(target = incoming).start()
    while True:
        message = input('Input message')
        if message == False:
            break
        s.sendall((message + '\n').encode())