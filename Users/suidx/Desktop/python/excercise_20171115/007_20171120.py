# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 06:27:18 2017
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
@author: suidx
"""
import os
import re
start_path='C:/Users/suidx/Desktop/python/excercise_data/'
files=os.listdir(start_path)
line_counts=0
total_line_counts=0
total_space_counts=0
space_counts=0
for file in files:
    print(file)
    with open(file,'r') as f:
        lines=f.readlines()
        for line in lines:
            line_counts+=1
            if line.isspace():
                space_counts+=1
        print(line_counts)
        print(space_counts)
    total_line_counts=total_line_counts+line_counts
    total_space_counts=total_space_counts+space_counts
print('total_line_counts:',total_line_counts)
print('total_space_counts:',total_space_counts)            
        