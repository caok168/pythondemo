import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0',8000))
server.listen()

def handler_sock(conn,addr):
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        input_data = input()
        conn.send(input_data.encode('utf-8'))

while True:
    conn,addr = server.accept()
    client_thread = threading.Thread(target=handler_sock,args=(conn,addr))
    client_thread.start()