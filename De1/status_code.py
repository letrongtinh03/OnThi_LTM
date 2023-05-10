# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:36:52 2023

@author: letro
"""

import requests

# Thay đổi url của trang web bạn muốn kết nối
url = 'https://google.com'

# Kết nối đến trang web
response = requests.get(url)

# In mã trạng thái
print(response.status_code)
