# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:11:22 2023

@author: letro
"""

# Lấy header của 1 url có sẵn
import gzip
import urllib.error
import urllib.request

if __name__ == '__main__':
    try:
        req = urllib.request.Request('https://vnexpress.net/')
        req.add_header('Accept-Encoding','gzip')
        res = urllib.request.urlopen(req)
        
        header = res.getheaders()
        print(header)
        text = gzip.decompress(res.read())
    except urllib.error.HTTPError as err:
        print(err.code)