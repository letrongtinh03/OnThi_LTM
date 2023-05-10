# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:38:50 2023

@author: letro
"""

import socket

# Tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thiết lập địa chỉ và cổng của server
server_address = ("localhost", 5555)

# Kết nối socket đến server_address
client_socket.connect(server_address)

# Nhập lệnh và hai số nguyên từ bàn phím
cmd = input("Enter command (Max/Min): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Gửi lệnh và hai số nguyên đến server
client_socket.send(f"{cmd} {a} {b}".encode())

# Nhận kết quả từ server và hiển thị lên màn hình
result = client_socket.recv(1024).decode()
print(f"Result: {result}")

# Đóng kết nối socket với server
client_socket.close()
