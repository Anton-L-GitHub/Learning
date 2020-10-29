import socket


SERVER = 'localhost'
PORT = 12345
SERVER_ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
BUFFSIZE = 1024

server_socket = socket.socket()
server_socket.connect(SERVER_ADDR)


message = input('> ').encode(FORMAT)
server_socket.send(message)
message = server_socket.recv(BUFFSIZE)
print(f'From server: {message.decode(FORMAT)}')
server_socket.close()
