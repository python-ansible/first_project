# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 06:30:57 2017

@author: suidx
"""

import xlwt
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
# indexing is zero based, row then column
sheet.write(0,1,'test text')
sheet.write(1,1,'test text')
wbk.save('test2.xls')  #默认保存在桌面上