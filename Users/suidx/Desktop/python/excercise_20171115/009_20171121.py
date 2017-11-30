# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:04:25 2017
第 0009 题： 一个HTML文件，找出里面的链接。
@author: suidx
"""
# coding=utf-8
from bs4 import BeautifulSoup
from urllib import urlopen 
 
def extract(path):
        doc = urlopen(path).read() 
        text = BeautifulSoup(doc, 'lxml')
        urls = text.findAll('a')
        for u in urls:
            print(u['href'])
        content = text.get_text().strip('\n')
        return content


if __name__ == '__main__':
    extract('https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html')