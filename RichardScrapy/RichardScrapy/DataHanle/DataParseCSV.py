# -*- coding: utf-8 -*-

import pymongo
import sqlite3
import sys
import csv
import codecs

# reload(sys)
#
# sys.setdefaultencoding('utf-8')

conn = pymongo.MongoClient('localhost', 27017)#创建连接
db = conn['NeihanDb']
collection = db['neihan_content']


csvfile = file('csv_test5.csv', 'wb')
# csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow(['mId','uId','content'])



i = 0
for msg in collection.find()[165000:185000]:
    if msg:

        # print msg["content"]
        i+=1
        print str(i) + "=================\n"
        uId = msg['uId']
        mId = msg['mId']
        uIcon = msg['uIcon']
        content = msg['content'].encode("utf-8")
        uName = msg['uName']

        # if (uId is None)|(mId is None)|(uIcon is None)|(content is None)|(uName is None):
        #     continue
        writer.writerow([mId,uId,content])
        # print str(uId)+'=='+str(mId)+'=='+uIcon+"=="+content+'=='+uName