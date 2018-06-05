# -*- coding: utf-8 -*-
import scrapy
from toscrape_books.items import BookItem
from scrapy.linkextractors import LinkExtractor

class BooksSpider(scrapy.Spider):
	name = "books"
	allowed_domains = ["toscrape.com"]
	start_urls = ['http://books.toscrape.com/catalogue/page-1.html']
	p=2
	def parse(self, response):
		le=LinkExtractor(restrict_css='article.product_pod')
		for link in le.extract_links(response):
			yield scrapy.Request(url=link.url,callback=self.books_parse)

		nextpage=LinkExtractor(restrict_css='ul.pager li.next')
		#nextpage.extract_links(response)[0].url
		link=nextpage.extract_links(response)
		if link:
			next_url=link[0].url
			yield scrapy.Request(url=next_url,callback=self.parse)

	def books_parse(self,response):
		book=BookItem()
		sel=response.xpath('//article[@class="product_page"]')
		book['bookname']=sel.css('div.product_main > h1 ::text').extract_first()
		book['price']=sel.xpath('.//p[@class="price_color"]/text()').extract_first()
		sel=response.xpath('//*[@id="content_inner"]/article/table')
		book['UPC']=sel.xpath('./tr[1]/td/text()').extract_first()
		#//*[@id="content_inner"]/article/table/tbody/tr[1]/td
		yield book