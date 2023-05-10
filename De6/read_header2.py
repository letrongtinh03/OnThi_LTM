# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:21:30 2023

@author: letro
"""

import requests
url = 'https://vnexpress.net/'
response = requests.head(url)
print(response.headers)
