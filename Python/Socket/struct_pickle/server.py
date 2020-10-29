import pickle
import socket
from utilss import pack
import struct

HOST = 'localhost'
PORT = 1235


sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen()
print('Waiting for connection')

while True:
    client_sock, client_addr = sock.accept()
    print(f'{client_addr}: Has connected!')

    message = [{'name': 'Anton', 'adress': 'Snigelvägen 3'}, {'name': 'Emma', 'adress': 'Djibberjabber 5'}]
    pic = pickle.dumps(message)
    print(len(pic))

    message = pack(message)
    client_sock.send(message)

