# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:47:52 2023

@author: letro
"""

import socket

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Định nghĩa host và port của server
host = '127.0.0.1'
port = 12345

# Kết nối đến server
client_socket.connect((host, port))

# Gửi lệnh và hai số nguyên đến server
command = input("Nhập lệnh (Add/Sub): ")
a = input("Nhập số a: ")
b = input("Nhập số b: ")

data = command + ' ' + a + ' ' + b
client_socket.send(data.encode())

# Nhận kết quả từ server
result = client_socket.recv(1024).decode()
print(f"Kết quả: {result}")

# Đóng socket
client_socket.close()
