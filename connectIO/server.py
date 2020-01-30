from typing import (
    Any, 
    Callable, 
    Optional
)

import pickle
import socket
import struct


class Server:

    def __init__(self, ip: str = '127.0.0.1', port: int = 5555) -> None:
        self.ip = ip
        self.port = port
        self.socket = socket.socket(
            socket.AF_INET, 
            socket.SOCK_STREAM
        )
        self.func = None

    def send(self, conn: 'socket.socket', data: Any) -> None:
        packets = pickle.dumps(data)
        value = socket.htonl(len(packets))
        size = struct.pack('L', value)

        conn.send(size)
        conn.send(packets)

    def recieve(self, conn: 'socket.socket') -> Any:
        size = struct.calcsize('L')
        size = conn.recv(size)
        size = socket.ntohl(struct.unpack('L', size)[0])

        result = b''

        while len(result) < size:
            result += conn.recv(size - len(result))

        return pickle.loads(result)

    def run(self) -> None:
        try:
            self.socket.bind((self.ip, self.port))

        except socket.error as e:
            print(e)

        else:
            print('Server sucessfully initialized')
            self.socket.listen()
            print('Server awaiting new connections')

            while True:
                try:
                    conn, addr = self.socket.accept()
                    print(f'Connection established to {addr}')

                    if self.func is not None:
                        self.func(conn, addr)

                except KeyboardInterrupt:
                    break
