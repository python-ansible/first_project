# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 07:12:32 2017

@author: suidx
"""

def filted_word(filename):
    word_list=[]#定义一个空列表
    with open(filename,'r') as f:#以读打开文件
        for line in f:#以行为单位遍历文件
            content = re.sub(r' ','',line)#替换掉空格符
            word_list.append(content.strip())#以行为单位添加进列表
    print(word_list)
    return word_list
def filer(input_word,f_file):
    if input_word in filted_word(f_file):#判断输入是否在列表中
        print('Freedom')
    else:
        print('Human Right')
add = 'C:/Users/suidx/Desktop/python/txt/filtered_words2.txt'
name = input('enter word:')#输入word
if __name__=='__main__':
    filer(name,add)