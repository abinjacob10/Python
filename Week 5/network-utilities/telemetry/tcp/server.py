"""Server
   Server opens up a socket using socket.socket(), binds the opened socket to an ip+port where client is trying to send "hi".
   Server listens to accept connections, uses accept() method to get socket object and address. This socket object is used to retrieve data and send back to client with a slight change.
"""
print(__doc__)


import socket
import ip

buffer=1024

#Assign 
addr1 = (ip.TCP1["server_ip"], ip.TCP1["port"])

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding the server to UDP port defined in ip.py file
socket1.bind(addr1)
#socket1.listen(1)
#Receiving data from client
while(True):
  #Listen
  socket1.listen(1)
  #Accept the incoming connection
  accept1, addr = socket1.accept()
  #separating socket object from address
  #sock_obj = accept1[0]
  #address = accept1[1]
  #Retrieving data from the object
  data = accept1.recv(buffer).decode()
  print(data)
  #print("11")
  data2=data + " Have a good day client."
  accept1.send(data2.encode())
  #print("12")
  #print("Message: {} from address {}".format(data,addr))
  #print("13")


