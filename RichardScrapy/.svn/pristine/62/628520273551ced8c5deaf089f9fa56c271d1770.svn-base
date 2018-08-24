# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import redis

# class RichardscrapyPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('DmozResult.json', 'wb', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         # item['title'] = self.stringTrip(item['title'])
#
#         print item['title']
#         line = json.dumps(dict(item)) + '\n'
#         self.file.write(line.decode("unicode_escape"))
#
#
#         return item
#
#     '''
#     字符串去空
#     '''
#     def stringTrip(self,content):
#         return content.replace('\n', "").replace('\r', "").replace("<br/>", "").replace("　", "").strip()
class DuplicatesPipeline(object):
    def __init__(self):
        self.r = redis.Redis(host='localhost',port=6379,db=0)

    def process_item(self, item, spider):
        if self.r.exists('id:%s' % item['mId']):
            print 'delete===='+item['content'].encode("utf-8")
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.r.set('id:%s' % item['mId'],1)
        return item



class RichardscrapyPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]



    def process_item(self, item, spider):
        # print item['content']
        self.collection.insert(dict(item))

        return item

    '''
    字符串去空
    '''
    def stringTrip(self,content):
        return content.replace('\n', "").replace('\r', "").replace("<br/>", "").replace("　", "").strip()