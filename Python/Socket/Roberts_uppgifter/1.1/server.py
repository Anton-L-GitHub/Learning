import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5050
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)
FORMAT = 'utf-8'

server_socket = socket.socket()  # No args = socket.AF_INET & socket.SOCK_STREAM
server_socket.bind(SERVER_ADDRESS)  # Binds socket to our SERVER_ADRESS


server_socket.listen()
print('Waiting for connections')


while True:
    client_socket, client_address = server_socket.accept()
    client_message = client_socket.recv(1024).decode()
    print(f'Message from {client_address[0]}: {client_message}')

    print('Sending back message to client...')
    client_socket.send(client_message.encode(FORMAT))
    client_socket.close()
    

