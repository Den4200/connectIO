# ConnectIO
A simple module for sending data across the internet!

## Use cases
- Multiplayer pygame games (sending objects)
- Chat server with multiple clients
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

        self.send(conn, response)
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
    print(f'From server: {resp1}')

    msg1 = 'hi server! how are you?'
    client.send(msg1)
    print(f'To server: {msg1}')

    resp2 = client.recieve()
    print(f'From server: {resp2}')

    msg2 = 'great thanks!'
    client.send(msg2)
    print(f'To server: {msg2}')

    client.close()

if __name__ == "__main__":
    main()
```
