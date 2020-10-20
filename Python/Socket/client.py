import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = "192.168.1.154"
ADDR = (SERVER, PORT)



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    user_message = input('> ')
    if user_message == DISCONNECT_MESSAGE:
        break
    else:
        send(user_message)
        continue