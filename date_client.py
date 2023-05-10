# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:44:48 2023

@author: letro
"""
# Nhập tháng và năm để xem tháng đó có bao nhiêu ngày
import socket

HOST = 'localhost'
PORT = 8080
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
    
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(ADDR)
    data = input("Enter month and year(month-year):")
    while True:
        if not data:
            break
        client_sock.send(str(data).encode('utf-8'))
        data = client_sock.recv(4096)
        print("Received from server: %s" %data.decode('utf-8'))
    client_sock.close()