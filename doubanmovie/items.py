# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    count=scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
    stra = scrapy.Field()
    quote = scrapy.Field()
