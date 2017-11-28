#!/usr/bin/python
"""
Created on Wed Nov 15 21:57:39 2017

@author: suidx
"""
'''
from skimage import io
img=io.imread('c:/timg.jpg')
io.imshow(img)
'''
from PIL import Image,ImageDraw, ImageFont
ttFont = ImageFont.truetype("arial.ttf", 100)
im = Image.open("c:/timg.jpg")  
draw = ImageDraw.Draw(im) 
draw.text((800,250),'3', fill=(255,0,0), font=ttFont)  
#draw.text((400,400),unicode('杨利伟','utf-8'), fill=(0,0,0), font=ttFont)  
im.show() 