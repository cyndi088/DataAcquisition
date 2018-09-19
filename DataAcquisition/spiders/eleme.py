# -*- coding: utf-8 -*-
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
        restaurants_parse_url = 'https://www.ele.me/restapi/shopping/restaurants?' \
                                'extras[]=activities&geohash=%s&latitude=%f&limit=24&' \
                                'longitude=%f&offset=%d&terminal=web'
        n = 0
        for data in data_list:
            n += 1
            geohash = data['geohash']
            latitude = data['latitude']
            longitude = data['longitude']
            request = Request(restaurants_parse_url % (geohash, latitude, longitude, 0),
                              callback=self.restaurants_parse, meta={'n': n}, dont_filter=True)
            yield request

    def restaurants_parse(self, response):
        n = response.meta['n']
        res = response.text
        restaurant_list = json.loads(res, encoding='gbk')
        i = 0
        for restaurant in restaurant_list:
            i += 1
            rest_id = str(restaurant['id'])
            latitude = restaurant['latitude']
            longitude = restaurant['longitude']
            info_url = 'https://www.ele.me/restapi/shopping/restaurant/%s?extras[]=flavors&extras[]=qualification&latitude=%f&longitude=%f&terminal=web'
            request = Request(info_url % (rest_id, latitude, longitude), callback=self.info_parse, dont_filter=True)
            # print('3333333333333333333333333333333')
            # print(n)
            # print(i)
            # print(rest_id)
            # print('4444444444444444444444444444444')
            yield request

    def info_parse(self, response):
        res = response.text
        print('*************************')
        print(res)
        print('*************************')

