# -*- coding: utf-8 -*-

import pymongo
import sqlite3
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

conn = pymongo.MongoClient('localhost', 27017)#创建连接
db = conn['NeihanDb']
collection = db['neihan_content']

cx = sqlite3.connect("Neihan.db")
cu = cx.cursor()
cu.execute('create table if not exists Neihan (id integer primary key,uId integer NULL,mId integer NULL,uIcon nvarchar(200) NULL,content nvarchar(1000) NULL, uName nvarchar(100) NULL)')


i = 0
for msg in collection.find():
    if msg:
        print str(i)+"=================\n"
        # print msg["content"]
        i+=1
        uId = msg['uId']
        mId = msg['mId']
        uIcon = msg['uIcon']
        content = msg['content']
        uName = msg['uName']

        # if (uId is None)|(mId is None)|(uIcon is None)|(content is None)|(uName is None):
        #     continue
        cu.execute("insert into Neihan values(%d, %d, %d, '%s', '%s','%s')"
                   %(i,0,0,uIcon,'',uName))
        # print str(uId)+'=='+str(mId)+'=='+uIcon+"=="+content+'=='+uName
cx.commit()