# -*- coding: utf-8 -*-
__author__ = 'ZZX'
__date__ = '2018.03.17'


import sys
import jieba
import jieba.analyse
from gensim.models import word2vec
model = word2vec.Word2Vec.load("../../data/ml.model")


def text_to_words(text, key_num):
    txt_key = jieba.analyse.extract_tags(text, key_num, withWeight=False)  # 从输入中提取关键词
    return txt_key


def calc(txt_key, factor):
    weight = []
    for index in range(len(txt_key)):
        weight.append(model.similarity(txt_key[index], factor[index]))
    ans = 0.0
    for i in weight:
        ans += i
    return ans


# kind从1开始
def load(factor_path, kind, key_num):
    f = open(factor_path)
    kind += 1
    while(1):
        ans = []
        kind -= 1
        f.readline()
        for i in range(key_num):
            str = f.readline()
            words = str.split()
            # print(words)
            ans.append(words[0])
        if kind == 0:
            return ans
        # print("---------------")
        # print(kind)


# 1.待比较文本 2.某一类共有多少关键词 3.比较关键词路径 4.共有多少类
def manager(text, key_num, factor_path, nkind):
    txt_key = text_to_words(text, key_num)
    value = []
    for kind in range(nkind):
        factor = load(factor_path, kind, key_num)
        value.append(calc(txt_key, factor))
    ans = 0
    big = 0
    for index in range(key_num):
        if value[ans] > big:
            big = value[ans]
            ans = index
    print("the kind is:" + str(ans) + "  weight is: " + str(big))


if __name__ == '__main__':
    # ans = load("../python-LDA/data/tmp/model_twords.dat", 2, 20)
    txt = "诊断依据：="+"1、病  史：发现肉眼血尿、尿有泡沫3周"+"2、症  状：患者3周前无明显诱因出现肉眼血尿1次，无明显双下肢水肿及眼睑浮肿，伴尿中泡沫增多。2周前于我院门诊就诊查尿常规示尿蛋白（++++）、红细胞（++++），尿沉渣提示尿红细胞满视野，为异常形态红细胞。24小时尿蛋白定量694mg/24h。血脂及肾功能均正常范围。腹部超声未见异常。予肾炎康复片等药物治疗。1天前复查24小时尿蛋白定量1732mg/24h。现为进一步诊治收入我科。"+"3、体  征：T 36.2℃ BP 120/70mmHg。双侧呼吸音清晰，双侧未闻及干湿性罗音和胸膜摩擦音。心率74次/分，律齐，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹软，无压痛、反跳痛、肌紧张，未触及包块，肝脾未及，Murfy氏征阴性，肠鸣音正常。双下肢无水肿。"+"4、辅助检查：我院尿微量总蛋白 1732(mg/24h尿)。ANCA阴性。免疫球蛋白G 1870.00(mg/dl)。类风湿因子 16.00(IU/mL)。自身抗体:抗SSA抗体 阳性、抗核抗体 阳性 S1:320。动态红细胞沉降率 27(mm/h)。尿常规:尿红细胞 250(++++)(/ul)、尿蛋白 150(+++)(mg/dl)。尿沉渣形态学分析:尿红细胞（镜检） 满视野(/HP)，主要为异常形态、大量细菌。血常规未见异常、HIV、TP未见异常。生化全项:白蛋白 31.0(g/L)、肝肾功血脂无异常。X线胸片提示双下肺纹理稍增重。腹部超声提示：肝内实性小结节，考虑血管瘤可能。"
    manager(txt,20,"../python-LDA/data/tmp/model_twords.dat",3)


