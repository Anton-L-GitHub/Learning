import socket
import struct
import pickle

HOST = 'localhost'
PORT = 1235

sock = socket.socket()
sock.connect((HOST, PORT))


while True:
    header = sock.recv(4)
    message_length,  = struct.unpack('!L', header)
    message_length = int(message_length - 4)
    message = sock.recv(message_length)
    message = pickle.loads(message)
    print(message)


