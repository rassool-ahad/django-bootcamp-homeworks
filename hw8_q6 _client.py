#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6000     # The port used by the server

from_lan = input("enter your text language:")
to_lan = input("enter to language you want translate:")
text = input("enter your text:")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(from_lan.encode()+"/".encode())
    s.send(to_lan.encode()+"/".encode())
    s.send(text.encode())
    data = s.recv(1024)

print('Received', repr(data.decode()))