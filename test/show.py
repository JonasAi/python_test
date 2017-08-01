# coding:utf-8
import pickle
import os
import numpy as np
import xlwt
# 该文件是批量反序列化操作的实验

def read(file):
    rf = pickle.load(open(file, "rb"))
    return rf

def read_path(path):
    files = os.listdir(path)
    L = []
    for file in files:
        if not os.path.isdir(file):
            rf =read(path+"/"+file)
            L.append(rf)
    test_write(L)

def test_write(line): # 501 个
    book = xlwt.Workbook() #创建一个Excel
    sheet1 = book.add_sheet('hello') #在其中创建一个名为hello的sheet
    line_num = len(line)+1 # 获取list 长度, +1 保留第一行做 title
    for i in line:
        line_num-=1
        x=0
        while x < len(i):
            sheet1.write(line_num,x,str(i[x]))
            x+=1
    book.save('/Users/jonas/Documents/Test/Python/train-bedroom.xls') #创建保存文件

#主函数
def main():
   read_path('/Users/jonas/Documents/Test/Python/train-bedroom')

if __name__=="__main__":
    main()

