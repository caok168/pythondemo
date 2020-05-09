import socket

server = socket.socket()
server.connect(('127.0.0.1',8000))
while True:
    input_data = input()
    server.send(input_data.encode('utf-8'))
    data = server.recv(1024)
    print(data.decode('utf-8'))