# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 职位名称：
    position = scrapy.Field()
    # 下一层网页链接：
    link = scrapy.Field()
    # 公司名称：
    company = scrapy.Field()
    # 职位月薪：
    salary = scrapy.Field()
    # 工作地点:
    workplace = scrapy.Field()
    # 最低学历：
    education = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()
    # 公司规模
    size = scrapy.Field()
    # 公司类型
    attribute = scrapy.Field()
    # 公司行业
    field = scrapy.Field()
    # 职位描述：
    description = scrapy.Field()
