from sys import path
from os.path import dirname

path.append(dirname(path[0]))
__package__ = 'example'


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
