import struct
import pickle


def pack(message):
    message_bytes = pickle.dumps(message)
    message_format = f'!L{len(message_bytes)}s'
    message_struct_size = struct.calcsize(message_format)
    message_packed = struct.pack(message_format, message_struct_size, message_bytes)
    return message_packed

