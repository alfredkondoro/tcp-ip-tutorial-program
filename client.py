import socket


c = socket.socket()

c.connect(('localhost', 9999))

if True:
    print(c.recv(1024).decode())

    while True:
        data = input('Input: ')
        if data == '#close':
            ins = '#close'
            c.send(bytes(ins, 'utf-8'))
            break
        else:
            c.send(bytes(data, 'utf-8'))
            print('Server:',c.recv(1024).decode())

c.close()
