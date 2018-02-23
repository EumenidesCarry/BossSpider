# encoding=utf-8


import scrapy
from ..items import BossspiderItem

class ZhiPinSpider(scrapy.Spider):
    name = 'BossSpider'
    start_urls = ['https://www.zhipin.com/c100010000/h_100010000/?query=Python&page={cnt}&ka=page-next'.format(cnt=cnt)
                  for cnt in range(1,10)]


    def parse(self, response):
        print(response)
        zp = BossspiderItem()
        post_list = response.xpath(".//*[@id='main']/div/div[2]/ul/li/div/div[1]/h3/a/div[1]/text()").extract()
        salary_list = response.xpath(".//*[@id='main']/div/div[2]/ul/li/div/div[1]/h3/a/span/text()").extract()
        # area_list = response.xpath(".//*[@id='main']/div/div[2]/ul/li/div/div[1]/p/text()").extract()
        # company_list = response.xpath(".//*[@id='main']/div/div[2]/ul/li/div/div[2]/div/h3/a/text()").extract()
        for p,s in zip(post_list,salary_list):
            zp['post'] = p
            zp['salary'] = s
            yield zp
