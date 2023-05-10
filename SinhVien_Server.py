# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:06:46 2023

@author: letro
"""

import socket

# Danh sách sinh viên
students = {
    "001": "John Doe",
    "002": "Jane Smith",
    "003": "Bob Johnson",
    "004": "Alice Lee"
}

# Tạo socket và liên kết địa chỉ IP và cổng
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 8888)
server_socket.bind(server_address)

# Lắng nghe kết nối đến
server_socket.listen(1)

print("Waiting for connection...")

while True:
    # Chấp nhận kết nối từ client
    client_socket, client_address = server_socket.accept()

    print(f"Connection from {client_address} has been established.")

    # Gửi lời chào đến client
    client_socket.sendall(b"Hello, welcome to the student information system.\n")

    # Gửi thông điệp để bắt đầu
    client_socket.sendall(b"Enter 1 to begin.\n")

    # Nhận yêu cầu từ client
    data = client_socket.recv(1024).decode().strip()

    if data == "1":
        # Yêu cầu nhập mã sinh viên
        client_socket.sendall(b"Please enter the student ID.\n")

        # Nhận mã sinh viên từ client
        student_id = client_socket.recv(1024).decode().strip()

        # Truy xuất thông tin sinh viên
        if student_id in students:
            student_name = students[student_id]
            client_socket.sendall(f"The student name is {student_name}.\n".encode())
        else:
            client_socket.sendall(b"Student not found.\n")

    # Đóng kết nối với client
    client_socket.close()
