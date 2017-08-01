#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
try:
    import cPickle as pickle
except ImportError:
    import pickle


def read_file(path):
    files=os.listdir(path)
    for file in files:
        s    = []
        f_new=""
        if not os.path.isdir(file):
            f = open(path+"/"+file)
            portion=os.path.splitext(file)
            f_new = path+"/"+portion[0]+".bow" # 这里是新的文件名处理
            iter_f=iter(f)
            str=""
            for line in iter_f:
                str=str+line
                s.append(str)
            pickle_str(s, f_new)
   # print(s)
   # return true

def pickle_str(a, filename):
    f = open(filename,'wb')
    pickle.dump(a,f)
    f.close
    #print(b)

a = read_file("/Users/jonas/Desktop/label-office")
#pickle_str(a)
