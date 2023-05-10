# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:52:07 2023

@author: letro
"""

import socket

def normalize_string(s):
    # remove trailing spaces
    s = s.strip()
    # convert to lowercase
    s = s.lower()
    # capitalize first letter after period
    s = ". ".join(map(lambda x: x.strip().capitalize(), s.split(".")))
    return s

HOST = '127.0.0.1' # địa chỉ IP của máy chủ
PORT = 65432 # cổng mà máy chủ sẽ lắng nghe

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Đang chờ kết nối từ client...")
    conn, addr = s.accept()
    with conn:
        print(f"Đã kết nối với {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Chuẩn hóa chuỗi và gửi lại cho client
            normalized_string = normalize_string(data.decode())
            conn.sendall(normalized_string.encode())
