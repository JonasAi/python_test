#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import urllib2
import os
def save_img(img_url,file_name,file_path='/Users/jonas/Downloads/img/'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print '文件夹',file_path,'不存在，重新建立'
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
        #下载图片，并保存到文件夹中
        urllib.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print '文件操作失败',e
    except Exception as e:
        print '错误 ：',e

file_name="/Users/jonas/Downloads/A.J._Buckley.txt";
file_obj=open(file_name,'r');
file_content=file_obj.read();

#url="http://www.open-open.com"
#s=urllib.urlopen(url).read()
#ss=s.replace(" ","")

#match=re.compile('[a-zA-z]+://[^\s]*\.(jpg|gif|png)');
match=re.compile('[a-zA-z]+://[^\s]*\.jpg');
urls=re.findall(match,file_content);
#save_path="/Users/jonas/Downloads/";
for i in urls:
    #print i
    #imgData = urllib2.urlopen(i).read();
    name=i.split("/")[-1];
    name=name.split(".")[0];
    #fileName=save_path+name;
    #urllib2.urlretrieve(i,fileName);
    #if os.path.exists(fileName):
     #   output = open(fileName,'wb+')
     #   output.write(imgData)
     #   output.close()
    save_img(i,name);
    print "Finished download \n"
else:
    print 'this is over'


