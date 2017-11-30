# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:34:39 2017

第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
@author: suidx
"""
'''
import re
def get_words():
    words=[]
    file_name='C:/Users/suidx/Desktop/python/txt/filtered_words.txt'
    #input=raw_input("Please input word:")
    #print(input)
    #matchflag=0
    with open(file_name,'r') as f:
        lines= f.readlines()
            #if input==word:
        for i in lines:
            words.append(i)
        return words
              #  print('Freedom')
             #   matchflag=1
    #if matchflag==0:
     #    print('Human Rights')       
    
def filter_words():
    input=raw_input("input word:")
    words=get_words()
    for i in range(len(words)):
        if re.match(input,words[i]):
            print('Freedom')
            return
    print('Human Rights')
    return
    
if __name__=='__main__':
    filter_words()
'''
#import sys
#reload(sys)
#defaultencoding = 'utf-8'
import re
import codecs
def read_words(filename='C:/Users/suidx/Desktop/python/txt/filtered_words2.txt'):
    words = []
    with codecs.open(filename,'r') as f:
        lines = f.readlines()
        for l in lines:
            words.append(l)
    return words

def filter_words():
    input = raw_input("Input: ")
    words = read_words()
    print(type(input))
    #input=input.encode('gbk')
    #input=input.decode('gbk').encode('utf-8')
    for i in range(len(words)):
        print(words[i])
        print('input:',input)
        if re.match(input, words[i]):
            print "Freedom"
            return
    print "Human Rights"
    return

filter_words()


  