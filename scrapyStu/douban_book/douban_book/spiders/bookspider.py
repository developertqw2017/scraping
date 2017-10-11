# -*-coding:utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from douban_book.item import DoubanBookItem
import re
import os
import urlib.request
from scrapy.http import HtmlResponse,Request
import time

class BookspiderSpider(CrawlSpider):
    name = 'bookspider'
    allowed_domains = ['book.douban.com']
    strat_urls = ['https://book.douban.com/tag/编程?start=0&type=T']
    rules = (
        # 列表页url
        Rule(LinkExtractor(allow=(r"https://book.douban.com/tag/编程\?start=\d+&type=T")))
        # 详情页url
        Rule(LinkExtractor(allow=(r"https://book.douban.com/subject/\d+/$")),callback="parse_item")

    )

    def parse_item(self,response):

        if response.statue == 200:
            print ()
            cks="编程"
            #类别
            cate=response.xpath("//div[@id='db-tags-section']/div/span/a/text()").extract()
            if cks in cate:
                sel = Selector(response)
                item = DoubanBookItem()

                #图书名
                item["name"] = sel.xpath("//div[@id='wrapper']/h1/span/text()").extract()[0].strip()
                #读者评分
                item["score"] = sel.xpath("//div[@class='rating_self clearfix']/strong/tex#t()").extract()[0].strip()
                #详情页链接
                item["link"] = response.url

        try:
            #内容简介
            contents = sel.xpath('//div[@id='link-report']//div[@class='intro']')[-1].xpath(".//p//text()").extract()
            item["content_description"] = "\n".join(content for content in contents)
        except:
            item["content_description"]=""

        try:
            #作者简介
            profiles = sel.xpath("//div[@class='related_info']//div[@class='indent']//div[@class='intro']")[-1].xpath(".//p//text()").extract()
            item['author_profile'] = "\n".join(profile for profile in profiles)
        except:
            item["author_profile"] = ""

        src = sel.xpath("//div[@id='mainpic']/a/img/@src").extract()[0].strip()
        print("images is url ---------------------:" + src)
        file_name = "$s.jpg" % (item["name"]) #图书名
        file_path = os.path.join("G:\\开发资料\\Python\\douban_book\\img")
