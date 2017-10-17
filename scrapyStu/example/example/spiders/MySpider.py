from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = "example.com"
    allowed_domains = ["hbagri.gov.cn"]
    start_url = [
        'http://www.hbagri.gov.cn/'
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('zwdt/*.htm',)),callback='parse'),


    )

    def parse(self,response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        name = response.xpath('//div[@class="article"]/text()').extract()
        print(name)

