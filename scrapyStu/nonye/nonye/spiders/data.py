# -*- coding: utf-8 -*-
import scrapy
from nonye.items import NonyeItem

class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['hbagri.gov.cn/zwdt/200019990.htm']
    start_urls = ('http://www.hbagri.gov.cn/zwdt/200019990.htm')

    def parse(self, response):

        item = Data()
        item['filenam'] = response.xpath('/html/body/div[1]/div[2]/comment()[1])').extract()
        yield item
