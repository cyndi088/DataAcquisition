# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class DataacquisitionPipeline(object):
    def process_item(self, item, spider):
        return item


class MongodbPipeline(object):
    def __init__(self, mongo_host, mongo_port, mongo_user, mongo_psw, mongo_db):
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_user = mongo_user
        self.mongo_psw = mongo_psw
        self.mongo_db = mongo_db

        # settings = get_project_settings()
        # self.client = MongoClient(
        #     host=settings['MONGO_HOST'],
        #     port=settings['MONGO_PORT'],
        #     username=settings['MONGO_USER'],
        #     password=settings['MONGO_PSW']
        # )
        # self.db = self.client[settings['MONGO_DB']]
        # self.coll = self.db[settings['MONGO_COLL']]

    @classmethod
    def from_crawler(cls, crawlder):
        return cls(
            mongo_host=crawlder.settings.get('MONGO_HOST'),
            mongo_port=crawlder.settings.get('MONGO_PORT'),
            mongo_user=crawlder.settings.get('MONGO_USER'),
            mongo_psw=crawlder.settings.get('MONGO_PSW'),
            mongo_db=crawlder.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(host=self.mongo_host, port=self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        cls = item.__class__.__name__
        if cls == 'CitiesItem':
            self.save_cities(item)
        # self.coll.save(dict(item))
        return item

    def save_cities(self, item):
        self.db['cites'].save(dict(item))
