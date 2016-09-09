# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class ZhrCmePipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    #构造函数，传入mongo的连接参数
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url=mongo_url
        self.mong_db=mongo_db
        
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url=crawler.settings.get("MONGO_URL"),
            mongo_db=crawler.settings.get("MONGO_DATABASE")        
        )
    #打开爬虫时所需的操作    
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_url)
        self.db=self.client[self.mong_db]
    #爬虫结束时的操作    
    def close_spider(self,spider):
        self.client.close()
    #此pipeline所要进行的操作    
    def process_item(self,item,spider):
        collection_name=item.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item