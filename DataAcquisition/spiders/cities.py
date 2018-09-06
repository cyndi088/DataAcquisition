# -*- coding: utf-8 -*-
import scrapy
import json
import geohash
from DataAcquisition.items import CitiesItem


class CitiesSpider(scrapy.Spider):
    name = 'cities'
    allowed_domains = ['www.ele.me/home/']
    start_urls = ['https://www.ele.me/restapi/shopping/v1/cities']

    def parse(self, response):
        res = json.loads(response.text, encoding='gbk')
        city = CitiesItem()
        for i in res:
            for data in res[i]:
                city['abbr'] = data['abbr']
                city['id'] = data['id']
                city['latitude'] = data['latitude']
                city['longitude'] = data['longitude']
                city['geohash'] = geohash.encode(data['latitude'], data['longitude'])
                city['name'] = data['name']
                city['pinyin'] = data['pinyin']
                yield city
