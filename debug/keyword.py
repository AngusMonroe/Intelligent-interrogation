# -*- coding:utf-8 -*-

import jieba
import pymssql

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = "47.94.12.***"
        self.user = "sa"
        self.pwd = "******"
        self.db = "Database"

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

ms = MSSQL(host="47.94.12.243",user="sa",pwd="Jiuyi8899",db="Database")
reslist = ms.ExecQuery("select 适应症 from data")
number = 1
for i in reslist:
    word = list(jieba.cut(str(i),cut_all=False))#精确模式
    for n in word:
        if n != '\'':
            InsertSQL="INSERT INTO keyword (name,num) VALUES ('"+ n +"',"+str(number)+")"
            print (InsertSQL)
            try:
                ms.ExecNonQuery(InsertSQL.encode('utf-8'))
            except  Exception:
                print('error')
                continue
    number += 1



