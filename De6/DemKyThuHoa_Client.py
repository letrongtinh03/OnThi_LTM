# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:03:42 2023

@author: letro
"""

# đếm số ký tự hoa
import socket

# Tạo socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ IP và port của server
server_address = ('localhost', 8888)

# Kết nối đến server
client_socket.connect(server_address)

# Nhập chuỗi từ bàn phím
string = input("Nhập chuỗi ký tự: ")

# Gửi chuỗi đến server
client_socket.sendall(string.encode())

# Nhận kết quả từ server và in ra màn hình
result = client_socket.recv(1024).decode()
print("Số ký tự hoa trong chuỗi là: ", result)

# Đóng kết nối
client_socket.close()
