# ConnectIO
A simple module for sending data across the internet!

## Use cases
- Multiplayer pygame games (sending objects)
- Chat server with clients
- Transferring files over a network
- Anything else you can think of!

## Installation
```cmd
pip install connectIO
```

## Simple Example
#### Server
```python
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
    ExampleServer().run()
```
#### Client
```py
from connectIO import Client

def main():
    client = Client()
    client.connect()

    resp1 = client.recieve()
    resp2 = client.send('hi server! how are you?')
    resp3 = client.send('great thanks!')

    client.close()


if __name__ == "__main__":
    main()
```
