# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 06:57:15 2017

@author: suidx
"""
'''
激活码一般是由26个大写字母和10个数字任意组合而成，长度为12位或者16位的居多。
一个激活码里的字符是可以重复的，而且必须要保证激活码是不能重复的。可以分别随机生成16个字符，
然后组成一个字符串，放在字典中，通过字典来判断是否有重复的激活码。
以下代码是用Python生成10个16位的激活码。
from numpy import random
num=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
activecode=dict()
code=''
for i in range(10):
    for j in range(17):
        k=random.randint(1,len(num))
        code=code+num[k]
    activecode[i]=code
    print(code+' ')
    code=''
    
'''    
#coding=utf-8  
import random  
import string  
  
def gene_activation_code(number,length):  
    '''
    @number:生成激活码的个数 
    @length:生成激活码的长度 
    '''  
    result = {}  
    source = list(string.ascii_uppercase)  
    for index in range(0,10):  
        source.append(str(index))  
    while len(result) < number:  
        key= ''  
        for index in range(length):  
            key += random.choice(source)  
        if key in result:  
            pass  
        else:  
            result[key] = 1  
    for key in result:  
        print key  
  
if __name__ == "__main__":  
    number = 10  
    length = 16  
    gene_activation_code(number,length)         