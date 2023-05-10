# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:39:31 2023

@author: letro
"""

import socket

def find_max_min(a, b, cmd):
    if cmd == "Max":
        return max(a, b)
    elif cmd == "Min":
        return min(a, b)

# Tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thiết lập địa chỉ và cổng của server
server_address = ("localhost", 5555)

# Kết nối socket đến server_address
server_socket.bind(server_address)

# Lắng nghe kết nối từ client
server_socket.listen(1)

print("Server is listening for incoming connections...")

while True:
    # Chấp nhận kết nối từ client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")

    # Nhận lệnh và hai số nguyên từ client
    cmd, a, b = client_socket.recv(1024).decode().split()
    a = int(a)
    b = int(b)

    # Tìm Max/Min và gửi kết quả về cho client
    result = find_max_min(a, b, cmd)
    client_socket.send(str(result).encode())

    # Đóng kết nối socket với client
    client_socket.close()
