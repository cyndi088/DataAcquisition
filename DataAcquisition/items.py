# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataacquisitionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CitiesItem(scrapy.Item):
    abbr = scrapy.Field()        # 城市略称
    id = scrapy.Field()          # 城市ID
    latitude = scrapy.Field()    # 经度
    longitude = scrapy.Field()   # 纬度
    geohash = scrapy.Field()     # 经纬度对应的geohash值
    name = scrapy.Field()        # 城市全称
    pinyin = scrapy.Field()      # 城市拼音
