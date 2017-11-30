
"""
Created on Tue Nov 28 06:03:42 2017
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
@author: suidx

#!/usr/bin/env Python
# coding=utf-8
import xlwt
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
count=0
# indexing is zero based, row then column
file='C:/Users/suidx/Desktop/python/txt/student2.txt'
with open(file) as f:
    content=f.read()
    dict=eval(content)
    for key,value in dict.items():
        print('key:',key)
        print('value:',value)
        count+=1
        sheet.write(count,0,key)
        for val in range(len(value)):
            sheet.write(count,val+1,value[val])
        wbk.save('test2.xls')
"""
#!/usr/bin/env Python
# coding=utf-8
import os
import json
import xlwt

# 存放文件的目录
filepath = 'C:/Users/suidx/Desktop/python/txt'
 
def run():
    os.chdir(filepath)
    # 读取文件内容
    with open('student2.txt') as f:
        content = f.read()
    # 转为json
    print(content)
    d = json.loads(content)
    file = xlwt.Workbook()
    # 添加sheet
    table = file.add_sheet('test')
    for row, i in enumerate(list(d)):
        table.write(row, 0, i)
        for col, j in enumerate(d[i]):
            table.write(row, col+1, j)
    file.save('student.xls')
 
if __name__ =="__main__":
    run()
