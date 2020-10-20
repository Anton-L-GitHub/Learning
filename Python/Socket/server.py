import socket
import threading
from threading import Thread


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')
    

    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
                connected = False
        
            print(f"[{addr}] - {msg}")
            conn.send('Msg recived'.encode(FORMAT))
    
    conn.close()


def start():
    server.listen()
    print(f'[LISTENING] Server is listening {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print('[STARTING] server is starting....')
start()
