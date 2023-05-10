# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:08:54 2023

@author: letro
"""

import socket

# Tạo socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ IP và port của server
server_address = ('localhost', 8888)

# Bind địa chỉ IP và port vào socket
server_socket.bind(server_address)

# Chờ kết nối từ client
server_socket.listen(1)
print("Đang chờ kết nối từ client...")

while True:
    # Chấp nhận kết nối từ client
    client_socket, client_address = server_socket.accept()
    print("Đã kết nối từ ", client_address)

    # Nhận chuỗi từ client
    data = client_socket.recv(1024).decode()
    print("Nhận được chuỗi ký tự: ", data)

    # Đếm số ký tự hoa trong chuỗi
    count = 0
    for char in data:
        if char.isupper():
            count += 1

    # Gửi kết quả về cho client
    client_socket.sendall(str(count).encode())

    # Đóng kết nối với client
    client_socket.close()
