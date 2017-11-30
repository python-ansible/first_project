# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:06:11 2017

@author: suidx
"""

import urllib
import urllib2
import re
def get_img_url(url):
    request=urllib2.Request(url)
    reference=urllib2.urlopen(request)
    page=reference.read()
    #regex=re.compile(r'<img.*?class="BDE_Image" .*? src="(.*?)".*?>') #编译正则匹配模式字符串
    regex=re.compile(r'<img.*? class="BDE_Image" src="(.*?)".*?>')
    img_url_list=re.findall(regex,page)
    return img_url_list

def get_url(urlist,path):
    for url in urlist:
        urllib.urlretrieve(url,'%s/%s.jpg'%(path,url[-8:-5]))
url='http://tieba.baidu.com/p/2166231880?see_lz=1' #爬虫页面
path='C:/Users/suidx/Desktop/python/image'  #存放路径
urlist=get_img_url(url)
get_url(urlist,path)