from base64 import encode
import socket
import threading

from requests import request

host = "0.0.0.0"
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("Listening on " + host + ":" + str(port))

def handle_client(client_socket, addr):
    while True:
        request = client_socket.recv(1024)
        if request.decode('utf-8') == "exit":
            client_socket.close()
            break
        print("[*] Received: " + request.decode('utf-8'))
        msg = "OK\n"
        client_socket.send(msg.encode())
        #for _ in addr:
        #    print(addr[_])

        #client_socket.close()

while True:
    client, addr = server.accept()
    print("[*] Accepted connection from " + str(addr[0]) + ":" + str(addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client, addr))
    client_handler.start()