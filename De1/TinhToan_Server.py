# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:48:26 2023

@author: letro
"""

import socket

# Khởi tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Định nghĩa host và port của server
host = '127.0.0.1'
port = 12345

# Liên kết host và port với socket
server_socket.bind((host, port))

# Lắng nghe kết nối
server_socket.listen()

print(f"Server đang lắng nghe trên {host}:{port}...")

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()

print(f"Đã kết nối với client: {client_address}")

# Nhận dữ liệu từ client và xử lý
while True:
    # Nhận lệnh và hai số nguyên từ client
    data = client_socket.recv(1024).decode()
    command, a, b = data.split()
    print('a : ' + a)
    print('b : ' + b)
    a, b = int(a), int(b)
    
    # Xử lý lệnh và gửi kết quả về cho client
    if command == 'Add':
        c = a + b
        result = str(c)
        client_socket.send(result.encode())
    elif command == 'Sub':
        c = a - b
        result = str(c)
        client_socket.send(result.encode())
    else:
        error_msg = "Lệnh không hợp lệ!"
        client_socket.send(error_msg.encode())
        
    # Nếu client gửi "exit" thì ngắt kết nối
    if data == "exit":
        break

# Đóng socket
client_socket.close()
server_socket.close()
