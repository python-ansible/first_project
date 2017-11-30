# -*- coding: utf-8 -*-
'''
Created on Thu Nov 16 21:23:04 2017
任一个英文的纯文本文件，统计其中的单词出现的个数
@author: suidx
'''
dict={}
import re
line_counts=0
char_counts=0
file_name='globaltimes.txt'
with open(file_name,'r') as f:
    lines=f.readlines()
for line in lines:
    line_counts=line_counts+1
    char_counts=char_counts+len(line)
    matchword=re.findall(r'[^A-Za-z0-9]+',line)
    #match =   re.findall(r'[^a-zA-Z0-9]+', line)
    for i in matchword:
        line=line.replace(i,' ')
    words=line.split()
    for i in words:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
 
print('line_counts:',line_counts)
print('char_counts:',char_counts)
for key,value in dict.items():
    print(key,value)