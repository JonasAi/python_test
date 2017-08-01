# coding:utf-8  
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np

frequency = np.zeros((9418,), dtype=np.int32)
  
#语料  
with open('/Users/jonas/Desktop/label-office/agan0003.txt') as f:
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

pickle.dump(frequency, open("/Users/jonas/Desktop/label-office/agan0003.bow",'wb'))

#pickle.load(open("/home/suiishii/Documents/svm-test-road/road0009.bow",'r+'))

#new = np.zeros((20,), dtype=np.int8)
