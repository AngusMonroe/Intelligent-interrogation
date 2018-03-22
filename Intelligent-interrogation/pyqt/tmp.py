import os
import fnmatch

root = "../../data/result/newdir/"

files = os.listdir(root)

# for filename in files:
#     # try:
#     print(filename)
#     if not fnmatch.fnmatch(filename, '*.txt'):
#         continue
#     oldpath = os.path.abspath(os.path.join(root, filename))
#     f = open(oldpath, "r", encoding="gbk")
#     txt = f.read()
#     print(txt)
txt1 = open(root + "40068631X2-0001458137-2-5-0-9.txt", "r", encoding="gbk").read()
txt2 = open(root + "40068631X2-0002976707-2-1-0-6.txt", "r", encoding="gbk").read()
txt3 = open(root + "40068631X2-0000300229-2-7-0-8.txt", "r", encoding="gbk").read()
txt4 = open(root + "40068631X2-0001443565-2-1-0-8.txt", "r", encoding="gbk").read()

print(txt1)
print(txt2)
print(txt3)
print(txt4)
