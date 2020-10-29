import socket

SERVER = 'localhost'
PORT = 12345
SERVER_ADDR = (SERVER, PORT)
BUFFSIZE = 1024
FORMAT = 'utf-8'


server_socket = socket.socket()
server_socket.bind(SERVER_ADDR)

server_socket.listen()
print('Waiting for connections')

while True:
    client_socket, client_addr = server_socket.accept()
    client_message = client_socket.recv(BUFFSIZE).decode(FORMAT)
    print(f'{client_addr[0]} says: {client_message}')

    print('Sending back message to client...')
    client_socket.send(client_message.encode(FORMAT))
    client_socket.close()



