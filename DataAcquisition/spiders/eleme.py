# -*- coding: utf-8 -*-
import scrapy
import json


class ElemeSpider(scrapy.Spider):
    name = 'eleme'
    allowed_domains = ['www.ele.me/home/']
    urls_list = []
    district_list = ['临安区', '西湖区', '上城区', '下城区', '拱墅区', '建德市', '萧山区', '富阳区', '江干区', '桐庐县', '淳安县', '余杭区', '滨江区']
    for district in district_list:
        urls_list.append('https://www.ele.me/restapi/v2/pois?extras[]=count&geohash=wtmknpnr9yy3&keyword=%s&limit=20&type=nearby' % district)
    start_urls = urls_list

    def parse(self, response):
        res = response.text
        print('*********************************************')
        print(json.loads(res, encoding='gbk')[0])
