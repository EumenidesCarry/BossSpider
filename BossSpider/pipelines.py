# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class BossspiderPipeline(object):
    #打开爬虫时，连接数据库connect('database_name')
    def open_spider(self,spider):
        self.con = sqlite3.connect("zhipin.sqlite")
        self.cu = self.con.cursor()


    def process_item(self, item, spider):
        #sql插入语句，将爬取的数据插入到数据库
        insert_sql = "insert into zhipin (post,salary,company,area,exp,edu,industry) VALUES ('{}','{}','{}','{}','{}','{}','{}')"\
            .format(item['post'],item['salary'],item['company'],item['area'],item['exp'],item['edu'],item['industry'])
        #执行插入语句
        self.cu.execute(insert_sql)
        #数据提交（数据插入或更新）需要commit
        self.con.commit()
        return item

    #爬虫结束时，数据库关闭
    def spider_close(self,spider):

        self.con.close()
