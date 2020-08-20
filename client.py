import socket

c = socket.socket()

c.connect(('localhost', 9999))

print(c.recv(1024).decode())

if True:
    name = input('Enter your name')
    c.send(bytes(name, 'utf-8'))

    print(c.recv(1024).decode())
