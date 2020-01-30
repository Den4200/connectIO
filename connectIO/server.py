from typing import Callable, Optional

from .client import Client


class Server(Client):

    def __init__(self, ip: str = '127.0.0.1', port: int = 5555) -> None:
        super(Server, self).__init__(ip, port)

    def run(self, func: Optional[Callable] = None) -> None:
        try:
            self.socket.bind((self.ip, self.port))

        except socket.error as e:
            print(e)

        else:
            print('Server sucessfully initialized')
            self.socket.listen()
            print('Server awaiting new connections')

            while True:
                conn, addr = self.socket.accept()
                print(f'Connection established to {addr}')

                if func is not None:
                    func(conn, addr)
