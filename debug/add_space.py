

import sys
sys.path.append('../')


input=open(r'/Users/xujiaxing/Downloads/jibingICD10.txt','r',encoding='utf8')  #打开文件
lines=input.readlines()   #读取文件
input.close()      #关闭文件
output=open(r'jibingICD','w',encoding='utf8')   #打开文件，其实这里，是创建文件。因为usb3.txt是不存在的
for line in lines:  #for循环
    if not line:     #如果不存在该行，就跳出循环
        break
    line=line.strip("\n")
    jing=line   #将当前行内容赋值给jing对象
    nf=line+' '+'\n'
    output.write(nf)  #write方法，写入到指定文件中
output.close()  #close关闭文件
print("done")
