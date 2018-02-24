# encoding=utf-8


import scrapy
#引入容器来保存所爬去的信息
from ..items import BossspiderItem

class ZhiPinSpider(scrapy.Spider):
    #设置唯一标示name
    name = 'BossSpider'
    #设置爬取的地址
    start_urls = ['https://www.zhipin.com/c100010000/h_100010000/?query=Python&page={cnt}&ka=page-next'.format(cnt=cnt)
                  for cnt in range(1,16)]

    def parse(self, response):
        '''
        爬取方法
        '''
        #实力一个容器保存爬取的信息
        zp = BossspiderItem()
        #爬取部分：使用xpath获取每个职位的li
        for posts in response.xpath(".//*[@id='main']/div/div[2]/ul/li/div"):
            #获取职位
            zp['post'] = posts.xpath(".//div[1]/h3/a/div[1]/text()").extract()[0]
            #获取工资
            zp['salary'] = posts.xpath(".//div[1]/h3/a/span/text()").extract()[0]
            #获取公司
            zp['company'] = posts.xpath(".//div[1]/h3/a/text()").extract()[-1]
            #获取地区
            zp['area'] = posts.xpath(".//div[1]/p/text()").extract()[0]
            #获取需求经验
            zp['exp'] = posts.xpath(".//div[1]/p/text()").extract()[1]
            #获取所需学历
            zp['edu'] = posts.xpath(".//div[1]/p/text()").extract()[2]
            #获取行业
            zp['industry'] = posts.xpath(".//div[1]/p/text()").extract()[3]
            #返回信息
            yield zp

