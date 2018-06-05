# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeBooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
	"""docstring for BookItem"""
	bookname=scrapy.Field()
	price=scrapy.Field()
	UPC=scrapy.Field()
	stock=scrapy.Field()
	reviews=scrapy.Field()