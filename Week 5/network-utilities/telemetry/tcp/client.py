"""CLient
   Client opens up a socket using socket.socket(), sends "hi" to an address defined in .connect() method.
   Continues to send "hi" every two seconds to server, until interruption is offerred by user. Note: Server has also same type(TCP) socket open and explicitly listening using listen()
"""
print(__doc__)
import ip
import time
#from datetime import datetime as dt
import socket
buffer=1024


addr1 = ip.TCP1["server_ip"] ,ip.TCP1["port"]
#print(addr1)
#data1 = dt.now()
#data = data1.encode('utf-8')
data ="hi"
#Creating new socket and new connection in Client in every iteration
while(True):
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect(addr1)
  #message_text = f"ATU {data1}"
  #Data is changed from String type to bytes type, because 1st argument in sendto() method accepts bytes
#  sock1.connect(addr1)
    message = data.encode()
  #message=bytes(output)
  #Sleep for 2 seconds 
  # Send data to the connected server socket.
    sock1.send(message)
  #print("6")
    data2 = sock1.recv(buffer)
    print("Message from server: {}".format(data2.decode()))
    time.sleep(1)
