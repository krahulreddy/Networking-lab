import socket 
import select 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.connect(('127.0.0.1', 8090)) 
  
while True:
    message = server.recv(2048) 
    print message 
    message = raw_input() 
    server.send(message) 
    print "<You>" , message
server.close()