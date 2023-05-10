# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:46:52 2023

@author: letro
"""

import socket
HOST = 'localhost'
PORT = 8080
BUFSIZ = 4096
ADDR = (HOST, PORT)
def resolve_data(data):
    lst = data.split('-')
    return cal_day(lst[0], lst[-1])
def cal_day(month, year):
    if month == '2':
        if int(year) % 4 == 0:
            return 29
        else:
            return 28
    if month in {'1','3','5','7','8','10','12'}:
        return 31
    else:
        return 30
    
        
if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        print('Server waiting for connection...')
        client_sock, addr = server_socket.accept()
        print('Client connected from: ', addr)
        while True:
            data = client_sock.recv(BUFSIZ)
            if not data:
                break
            print("Received from client: %s" % data.decode('utf-8'))
            data_sent = resolve_data(data.decode('utf-8'))
            client_sock.send(str(data_sent).encode('utf-8'))
            break
        client_sock.close()
    server_socket.close()        
            