from sys import path
from os.path import dirname

path.append(dirname(path[0]))
__package__ = 'example'


from connectIO import Server, threaded

class ExampleServer(Server):

    def __init__(self, ip='127.0.0.1', port=5555):
        super(ExampleServer, self).__init__(ip, port)
        self.func = self.threaded_conn

    @threaded
    def threaded_conn(self, conn, addr):
        raddr = conn.getpeername()

        greeting = 'hello client!'
        print(f'Server -> {raddr}: {greeting}')

        self.send(conn, greeting)
        print(f'{raddr} -> Server: {self.recieve(conn)}')

        response = 'great you?'
        print(f'Server -> {raddr}: {response}')

        resp2 = self.send(conn, response)
        print(f'{raddr} -> Server: {self.recieve(conn)}')

if __name__ == "__main__":
    server = ExampleServer()
    server.run()
