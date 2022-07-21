import socket

host = '127.0.0.1'
port = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"Hello, World!")
    data = s.recv(1024)

print(f"Received {data}!r")
