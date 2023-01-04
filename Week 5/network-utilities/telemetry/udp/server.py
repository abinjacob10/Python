"""Server
   Server opens up a socket using socket.socket(), binds the opened socket to an ip where client is trying to send "hi"
   Receives data using .recvfrom() method. 
   Prints message and ip separately for brevity
"""



import socket
import ip

buffer=1024

addr1 = (ip.UDP1["server_ip"], ip.UDP1["port"])
print(addr1)




socket1=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Binding the server to UDP port defined in ip.py file
socket1.bind(addr1)

#Receiving data from client
while(True):
  #receive method is accessed to retrieve data
  data = socket1.recvfrom(buffer)
  #separate message from ip address
  message = data[0]
  address = data[1]

  print("Message: {} from address {}".format(message,address))



