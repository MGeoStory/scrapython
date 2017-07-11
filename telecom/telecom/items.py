# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class HinetStoreItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    name = scrapy.Field()
    storeType = scrapy.Field()
    address= scrapy.Field()
    # pass

class TFNStoreItem(scrapy.Item):
    storeType = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()