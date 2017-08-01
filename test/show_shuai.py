# coding:utf-8
import pickle
import os
import numpy as np
import xlwt

def read(file):
    list = pickle.load(open(file, "rb"))
    test('E:\Master research\\da.xls',list)
    print list

def read_path(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            read(path+"/"+ file)

def test(new_file , list):
    book = xlwt.Workbook() #创建一个Excel
    sheet1 = book.add_sheet('hello') #在其中创建一个名为hello的sheet
    j = 0
    while j < 500:
        i = 0 #列序号 
        for app in list : #遍历list每一行
        
            sheet1.write(j, i, app) #在新sheet中的第i行第j列写入读取到的x值
              
            i = i + 1 #行号递增、
        j = j + 1
    print i
    print j
    book.save(new_file)   
       
read_path("E:\\Master research\\train-bedroom")