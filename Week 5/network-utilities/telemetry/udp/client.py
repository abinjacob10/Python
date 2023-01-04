"""CLient
   Client opens up a socket using socket.socket(), sends "hi" to an address defined in .sendto() method.
   Continues to send "hi" every two seconds to server, until interruption is offerred by user. Note: Server has also same type(DGRAM) socket open and bound(listening) to same addresss+port
"""
print(__doc__)
import ip
import time
#from datetime import datetime as dt
import socket


addr1 = ip.UDP1["server_ip"] ,ip.UDP1["port"]
#print(addr1)
#data1 = dt.now()
#data = data1.encode('utf-8')
data ="hi"
#Created socket only once for the client not numerous times inside while loop, same goes with server.
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
  #message_text = f"ATU {data1}"
  #Data is changed from String type to bytes type, because 1st argument in sendto() method accepts bytes
  message = str.encode(data)
  #message=bytes(output)
  #Sleep for 2 seconds 
  time.sleep(2)
  # Send data(1st argument) to the server's address(2nd argument). NOte: server address(addr1) has both dotted decimal notation ipv4 and port number
  sock1.sendto(message,addr1)
