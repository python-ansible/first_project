# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 06:30:59 2017
第 0008 题：一个HTML文件，找出里面的正文。
@author: suidx
"""

#!/usr/bin/env python
#coding: utf-8
from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 要分析的网页url
url = 'http://finance.ifeng.com/a/20171120/15806563_0.shtml'

def extract(url):
    '''
    提取网页正文
    '''
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == '__main__':
    print extract(url)
'''
