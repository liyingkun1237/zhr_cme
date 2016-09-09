# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhrCmeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name=scrapy.Field()    
    product_code=scrapy.Field()
    contract_month=scrapy.Field()
    first_notice=scrapy.Field()
    last_trade=scrapy.Field()
