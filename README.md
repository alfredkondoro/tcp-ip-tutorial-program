# tcp-ip-tutorial-program
Application that implements TCP/IP
Create 2 files
1. server.py
2. Client.py


Use 2 conventions
1. s - for server.
2. c - for client.


server.py
---------
* Import socket module for socket programming.
import socket


* Use the socket() function to create a socket.
s = socket.socket()
print('Socket Created')


* Use the bind() function to bind an ip address to a port.
s.bind(('localhost', 9999))


* Use the listen() function to listen for connection and provide status “waiting to connect”.
s.listen(3)
print('Waiting for connections') 


* While loop to accept connection, the recv() function to accept name from the client and decode() to turn byte format to string. Then print the status and send() function to welcome the client with bytes() function that formats the message.
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()


    print("Connected with", addr, name)
   
    c.send(bytes('Welcome to Alfreds Server', 'utf-8'))


* Close the connection
c.close()

===========================================================================================================================================

client.py
---------
* Import socket module for socket programming.
import socket


* Use the socket() function to create a socket.
c = socket.socket()


* Use the connect() function since the client does not need to bind to address. The connect function helps to connect to the server.
s.connect(('localhost', 9999))


* Allow the user to enter the name and the send() function to send to the server the name. The bytes() function to format the message.
name =input("Enter your name")
c.send(bytes(name,'utf-8'))
