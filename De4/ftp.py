# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:08:51 2023

@author: letro
"""

import ftplib

# Kết nối tới site FTP
ftp = ftplib.FTP("file:///D:/The_Third_Year_Semester_2/Network_Programing/DeThi/")
ftp.login("letrongtinh03@gmail.com","241022")

# Lấy danh sách các thư mục
directories = []
ftp.dir(directories.append)

# In danh sách các thư mục
print("Danh sách các thư mục:")
for directory in directories:
    print(directory)

# Lấy danh sách các tập tin
files = ftp.nlst()

# In danh sách các tập tin
print("Danh sách các tập tin:")
for file in files:
    print(file)

# Ngắt kết nối tới site FTP
ftp.quit()
