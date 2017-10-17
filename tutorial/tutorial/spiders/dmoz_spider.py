#-*-coding:UTF-8-*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor

class DmozSpider(CrawlSpider):

    name = "dmoz"
    tags=("武陵山片区","富硒","茶叶","农产品","茶园","农业",
          "有机","恩施","茶业","走马","骑龙","绿色","邬阳乡",
          "茶农","茶苗","春茶","片区","鑫农")
    kw = {"武陵山片区": 1,
        "富硒":         1,
        "茶叶":         0.102492,
        "农产品":       0.076558,
        "茶园":         0.039464,
        "农业":         0.035655,
        "有机":         0.035529,
        "恩施":         0.024244,
        "茶业":         0.018679,
        "走马":         0.015901,
        "骑龙":         0.012651,
        "绿色":         0.012634,
        "邬阳乡":       0.009488,
        "茶农":         0.009021,
        "茶苗":         0.008223,
        "春茶":         0.008165,
        "片区":         0.008085,
        "鑫农":         0.007591
        }
    kwall = 0
    start_urls = [

        "http://www.xianfeng.gov.cn/xfyw/index.jhtml"

    ]

    rules = (
        Rule(LinkExtractor(allow=(r'xfyw/[0-9]{5}\.jhtml$')), callback='parse_1', follow=True),
    )

    def parse_1(self, response):
        for sel in response.xpath('//div[@class="content"]'):
            title = sel.extract()
            for tag in self.tags:
                if title.encode("UTF_8").find(tag) != -1:
                    self.kwall = self.kwall + self.kw[tag]
                else:
                    self.kwall = self.kwall + 0

            print(self.kwall)

            #if self.kwall > 0.7:
            #    print(title.encode("UTF_8"))
            self.kwall = 0
