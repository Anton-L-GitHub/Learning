import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5050
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)
FORMAT = 'utf-8'

# Create connection
server_connection = socket.socket() # No args = socket.AF_INET & socket.SOCK_STREAM
server_connection.connect(SERVER_ADDRESS)

message = input('> ')

server_connection.send(message.encode())

messsage_from_server = server_connection.recv(1024).decode()

print(messsage_from_server)