import socket
host = '127.0.0.1'
port = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((host,port)) 
    welcom = s.recv(1024).decode()
    print(welcom)
    while True:
        massage = input('input massage')
        if massage == False:
            break
        s.sendall((massage + '\n').encode())
        response = s.recv(1024).decode()
        print(f'Response from {host}: {response}')
    print('disconect')
    

