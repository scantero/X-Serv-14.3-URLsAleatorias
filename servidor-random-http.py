#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 8080))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)


try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        print recvSocket.recv(1024)
        
        num_aleatorio = random.randint(11111, 99999)

        html = '<html><body><a href="http://localhost:8080/'
        html += str(num_aleatorio)
        html += '">Dame otra</a></body></html>'

        respuesta = 'HTTP/1.1 200 OK\r\n\r\n'
        respuesta += html
        respuesta += '\r\n'
        
        recvSocket.send(respuesta)
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binding socket"
    mySocket.close()
    
    
    
    
