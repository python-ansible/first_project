# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 08:18:55 2017

@author: suidx
"""
from PIL import Image
import os
import re
#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#读照片
Start_path='C:/Users/suidx/Desktop/python/image/'
iphone5_width=1136
iphone5_depth=640
list=os.listdir(Start_path)
for i in list:
    path=Start_path+i
    print('path',path)
    print('i:',i)
    im=Image.open(path)
    x,y=im.size
    if x>iphone5_width:
        print(i)
        print('图片名称为'+i+'被修改')
        y=iphone5_width*y/x
        x=iphone5_width
        out=im.resize((x,y),Image.ANTIALIAS)
        new_pic=re.sub(i[:-4],i[:-4]+'_new',i)
        new_path=Start_path+new_pic
        print('new_pic',new_pic)
        print('new_path',new_path)
        out.save(new_path)
        
    if y>iphone5_depth:
        print(i)
        print('图片名称为'+i+'被修改')
        y=iphone5_depth
        x=iphone5_depth*x/y
        out=im.resize((x,y),Image.ANTIALIAS)
        new_pic=re.sub(i[:-4],i[:-4]+'_new',i)
        new_path=Start_path+new_pic
        print(new_path)
        out.save(new_path)