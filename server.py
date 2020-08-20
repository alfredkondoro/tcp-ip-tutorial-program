import socket

# create the socket
s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Ready waiting for connections')

while True:

    c, addr = s.accept()

    print("Connected with", addr)
    c.send(bytes('Welcome to Alfreds Server', 'utf-8'))

    while True:
        ins = c.recv(1024).decode()
        if ins == 'yes':
            c.close()
            close = input('The client has closed connection, kindly close yours(y/n)')
            if close == 'y':
                print('Closing...')
                s.close()
                print('Closed')
                break
        else:
            print('Client:', ins)
            reply = input('Server: ')
            c.send(bytes(reply, 'utf-8'))
            continue
