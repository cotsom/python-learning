from socket import *

host = '127.0.0.1'
port = 1234
socket = socket(AF_INET, SOCK_STREAM)
socket.bind((host, port))
socket.listen()

conn, addr = socket.accept()
print(f"Connected by {addr}")
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    #conn.sendall(data)