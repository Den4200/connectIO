import pickle
import socket
import struct


class Client:

    def __init__(self, ip: str = '127.0.0.1', port: int = 5555) -> None:
        self.ip = ip
        self.port = port
        self.socket = socket.socket(
            socket.AF_INET, 
            socket.SOCK_STREAM
        )
        self.addr = (self.ip, self.port)

    def connect(self) -> None:
        self.socket.connect(self.addr)

    def recieve(self):
        size = struct.calcsize('L')
        size = self.socket.recv(size)
        size = socket.ntohl(
            struct.unpack('L', size)[0]
        )

        result = b''

        while len(result) < size:
            result += self.socket.recv(size - len(result))

        return pickle.loads(result)

    def send(self, data):
        packets = pickle.dumps(data)
        value = socket.htonl(len(packets))
        size = struct.pack('L', value)
        self.socket.send(size)
        self.socket.send(packets)
        
        return self.recieve()
