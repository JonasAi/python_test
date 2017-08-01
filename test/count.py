# coding:utf-8  
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np
import os


def test_1(file, new_file):
    frequency = np.zeros((9418,), dtype=np.int32)  
		#语料

    with open(file) as f:
         count = f.readlines()
		  
		#将文本中的词语转换为词频矩阵  
         vectorizer = CountVectorizer()  
		#计算个词语出现的次数  
         X = vectorizer.fit_transform(count)  
		#获取词袋中所有文本关键词  
         word = vectorizer.get_feature_names()
    print (word)
		#查看词频结果
    X = X.toarray()
    print (X)

    for i in range(0, len(word)):
        frequency[int(word[i])] = X[0][i]

    pickle.dump(frequency, open(new_file,'wb'))

		#pickle.load(open("/home/suiishii/Documents/svm-test-road/road0009.bow",'r+'))

		#new = np.zeros((20,), dtype=np.int8)

def read_file(path):
    files=os.listdir(path)
    for file in files:
        f_new=""
        if not os.path.isdir(file):
            portion=os.path.splitext(file)
            f_new = path+"/"+portion[0]+".bow" # 这里是新的文件名处理
            test_1(path+"/"+file,f_new)
# 此处定义处理文件目录
read_file("/Users/jonas/Desktop/label-office")