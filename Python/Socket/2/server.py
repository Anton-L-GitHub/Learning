import socket

# Create a socket, no args = ipv4 & sock_stream
server = socket.socket()
# Spec what ip and port for socket
server.bind(('localhost', 8080))


server.listen(3)
print('Waiting for connections...')

while True:
    client, c_address = server.accept()
    print('Connected with', c_address[0])
    name = client.recv(1024).decode()
    client.send(bytes(f'Hello there {name}', 'utf-8'))

    client.close()

