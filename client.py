#!/usr/bin/env python3

import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

        print('Received', repr(data))
        os.system('echo "True" > pc_1.txt')

    except socket.error:

        print("Ot mean connection!!")
        os.system('echo "False" > pc_1.txt')

