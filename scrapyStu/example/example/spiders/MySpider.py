import scrapy
import scrapy.spider import CrawlSpider, Rule
import scrapy.linkextractors import LinkExtractor



class MySpider(scrapy.spiders.Spider):
    name = "example.com"
    allowed_domains = ["example.com"]
    start_url = [
        'http://www.example.com'
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('category\.php',)),callback='parse_item'),


        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php',)),callback='parse_item'),
    )

    def parse(self,response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID:(\d+)')
        item['name'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item


