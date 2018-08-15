# -*- coding: utf-8 -*-
import scrapy


class ElemeSpider(scrapy.Spider):
    name = 'eleme'
    allowed_domains = ['www.ele.me/home/']
    start_urls = ['http://www.ele.me/home//']

    def parse(self, response):
        pass
