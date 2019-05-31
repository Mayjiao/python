# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcaseItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        #filename = "teacher.html"
        #open(filename, 'w').write(response.body)
        item = ItcaseItem()
        context = response.xpath('/html/body/div[1]/div[5]/div[2]/div[3]/ul/li[2]/div[2]')
        item['name'] = context.extract()
        #title = context.extract_first()
        #print(title)
        yield item
        #pass
