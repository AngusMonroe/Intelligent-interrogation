__author__ = 'XJX'
__date__ = '2017.08.02'

import sys
from gensim.models import word2vec
import logging  
   
file = r'../data/data.txt'

#print(os.sys.path)
   
# 主程序  
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)  
sentences =word2vec.Text8Corpus(file)  # 加载语料  
model =word2vec.Word2Vec(sentences, size=200)  #训练skip-gram模型，默认window=5  
   
print(model)  
# 计算两个词的相似度/相关程度  
try:  
    y1 = model.similarity(u"高血压", u"头痛")  
except KeyError:  
    y1 = 0  
print (u"【高血压】和【头痛】的相似度为："+str(y1))
print("-----\n")  

# 计算某个词的相关词列表  
y2 = model.most_similar(u"高血压", topn=20)  # 20个最相关的  
print (u"和【高血压】最相关的词有：\n")  
for item in y2:  
    print(item[0], item[1]) 
print("-----\n")
   
# 保存模型，以便重用  
model.save(u"ml.model")  
# 对应的加载方式  
# model_2 =word2vec.Word2Vec.load("text8.model")  
   
# 以一种c语言可以解析的形式存储词向量  
#model.save_word2vec_format(u"书评.model.bin", binary=True)  
# 对应的加载方式  
# model_3 =word2vec.Word2Vec.load_word2vec_format("text8.model.bin",binary=True)  
