# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 08:01:12 2017
**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
@author: suidx
"""
import os
import re
from collections import Counter 
file_path='C:/Users/suidx/Desktop/python/dairy/'
files=os.listdir(file_path)
#过滤词  
stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 'this','s', 'is', 'are', 'a', 'with', 'as']
words={}
for file in files:
    content=open(file_path+file,'r')
    content=''.join(content.readlines())
    '''
    lines=content.readlines()
    for line in lines:
        match=re.findall(r'[^A-Za-z0-9]+',line)
        for i in match:
            line=line.replace(i,' ')
        word=line.split()
        for w in word:
            if w not in words:
                words[w]=1
            else:
                words[w]=words[w]+1
    '''
    pat = '[a-z0-9\']+'  
    words = re.findall(pat, content)  
    wordList = Counter(words)  
    for s in stop_word:
        wordList[s]=0
    print('file',file)
    #for key,value in words.items():
        #print(key,':',value)   
    #max_val=max(words,key=words.get)
    max_val=wordList.most_common()[0]
    print('max_val:',max_val)             