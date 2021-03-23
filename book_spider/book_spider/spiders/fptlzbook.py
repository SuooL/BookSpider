# -*- coding: utf-8 -*-
import scrapy


class FptlzbookSpider(scrapy.Spider):
    name = 'fptlzbook'
    allowed_domains = ['lnlyyz.com']
    start_urls = ['http://lnlyyz.com/']

    def parse(self, response):
        pass
