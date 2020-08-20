import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connections')

while True:
    c, addr = s.accept()

    print("Connected with", addr)
    c.send(bytes('Welcome to Alfreds Server', 'utf-8'))

    name = c.recv(1024).decode()
    print("Our client\'s name is", name)
    c.close()
