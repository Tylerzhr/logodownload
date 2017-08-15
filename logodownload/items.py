# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imagUrl=scrapy.Field()
    imagName=scrapy.Field()
    image=scrapy.Field()
