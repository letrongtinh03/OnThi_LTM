# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:06:16 2023

@author: letro
"""

import socket

# Tạo socket và kết nối đến server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 8888)
client_socket.connect(server_address)

# Nhận lời chào từ server
print(client_socket.recv(1024).decode())

# Nhận thông điệp để bắt đầu
print(client_socket.recv(1024).decode())

# Gửi yêu cầu để bắt đầu
client_socket.sendall(b"1\n")

# Nhận yêu cầu nhập mã sinh viên
print(client_socket.recv(1024).decode())

# Nhập mã sinh viên
student_id = input("Enter the student ID: ")

# Gửi mã sinh viên đến server
client_socket.sendall(f"{student_id}\n".encode())

# Nhận thông tin sinh viên từ server
response = client_socket.recv(1024).decode()
print(response)

# Đóng kết nối với server
client_socket.close()
