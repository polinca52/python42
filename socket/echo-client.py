import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    host = '127.0.0.1'
    port = 5000
    s.connect((host,port)) 
    s.sendall(b'hello world') 
    date = s.recv(1024)
    print(date)

   