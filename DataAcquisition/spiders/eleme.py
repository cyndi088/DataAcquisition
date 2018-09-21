# -*- coding: utf-8 -*-
import time
import random
import scrapy
import json
from scrapy import Request
from DataAcquisition.items import RestaurantItem


class ElemeSpider(scrapy.Spider):
    name = 'eleme'
    allowed_domains = ['www.ele.me/home/', 'www.ele.me/']
    urls_list = []
    district_list = ['临安区']
    for district in district_list:
        urls_list.append('https://www.ele.me/restapi/v2/pois?extras[]=count&'
                         'geohash=wtmknpnr9yy3&keyword=%s&limit=20&type=nearby' % district)
    start_urls = urls_list

    def parse(self, response):
        res = response.text
        data_list = json.loads(res, encoding='gbk')
        # restaurants_parse_url = 'https://www.ele.me/restapi/shopping/restaurants?' \
        #                         'extras[]=activities&geohash=%s&latitude=%f&limit=24&' \
        #                         'longitude=%f&offset=%d&terminal=web'
        restaurants_parse_url = 'https://mainsite-restapi.ele.me/pizza/v3/restaurants?offset=%d&limit=10&' \
                                'latitude=%f&longitude=%f&extras=["activities"]&' \
                                'extra_filters=home&keyword=&order_by=0&terminal=weapp&user_id=1817989241'
        n = 0
        offset = 0
        for data in data_list:
            n += 1
            print('-----------------------------------------------------')
            print(data)
            print('-----------------------------------------------------')
            geohash = data['geohash']
            latitude = data['latitude']
            longitude = data['longitude']
            # request = Request(restaurants_parse_url % (geohash, latitude, longitude, 0),
            #                   callback=self.restaurants_parse, meta={'n': n}, dont_filter=True)
            request = Request(restaurants_parse_url % (offset, latitude, longitude),
                              callback=self.restaurants_parse, meta={'n': n, 'offset': offset, 'latitude': latitude,
                                                                     'longitude': longitude}, dont_filter=True)
            yield request

    def restaurants_parse(self, response):
        restaurants_parse_url = 'https://mainsite-restapi.ele.me/pizza/v3/restaurants?offset=%d&limit=10&' \
                                'latitude=%f&longitude=%f&extras=["activities"]&' \
                                'extra_filters=home&keyword=&order_by=0&terminal=weapp&user_id=1817989241'
        n = response.meta['n']
        offset = response.meta['offset']
        latitude = response.meta['latitude']
        longitude = response.meta['longitude']
        res = response.text
        data_list = json.loads(res, encoding='utf-8')
        # print('*****************************')
        # print(info_list['items'])
        # print('*****************************')
        i = 0
        shop = RestaurantItem()
        if data_list['items']:
            for data in data_list['items']:
                i += 1
                info = data['restaurant']
                shop['address'] = info['address']
                shop['authentic_id'] = info['authentic_id']
                shop['description'] = info['description']
                shop['id'] = info['id']
                shop['image_path'] = info['image_path']
                shop['latitude'] = info['latitude']
                shop['longitude'] = info['longitude']
                shop['name'] = info['name']
                shop['opening_hours'] = info['opening_hours']
                shop['phone'] = info['phone']
                shop['rating'] = info['rating']
                shop['rating_count'] = info['rating_count']
                shop['recent_order_num'] = info['recent_order_num']
                shop['status'] = info['status']
                shop['type'] = info['type']
                print('3333333333333333333333333333333')
                print(n)
                print(i)
                print(shop)
                print('4444444444444444444444444444444')
                # time.sleep(random.random() * 2)
                yield shop
            offset += 10
            request = Request(restaurants_parse_url % (offset, latitude, longitude),
                              callback=self.restaurants_parse, meta={'n': n, 'offset': offset, 'latitude': latitude,
                                                                     'longitude': longitude}, dont_filter=True)
            # time.sleep(random.random() * 2)
            yield request
        else:
            pass

    def info_parse(self, response):
        pass
