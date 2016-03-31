# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class coding_calendarItem(scrapy.Item):
    codename = scrapy.Field()
    name = scrapy.Field()
    st = scrapy.Field()
    et = scrapy.Field()
    link = scrapy.Field()
    dur = scrapy.Field()
