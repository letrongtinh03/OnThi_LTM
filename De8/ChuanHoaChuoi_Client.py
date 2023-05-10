# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:52:45 2023

@author: letro
"""

import socket

HOST = '127.0.0.1' # địa chỉ IP của máy chủ
PORT = 65432 # cổng mà máy chủ sẽ lắng nghe

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # Nhập chuỗi từ client
        message = input("Nhập chuỗi: ")
        # Gửi chuỗi đến server
        s.sendall(message.encode())
        # Nhận chuỗi được chuẩn hóa từ server
        normalized_string = s.recv(1024).decode()
        print(f"Chuỗi được chuẩn hóa: {normalized_string}")
