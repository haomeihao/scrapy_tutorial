#! D:\setup\Python27 python27
# coding:utf-8

import scrapy

class ArticleItem(scrapy.Item):
    author = scrapy.Field()
    stats = scrapy.Field()
    content = scrapy.Field()

class ArticleSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        article = ArticleItem()
        article['author'] = response.xpath("//div[@class=author]/a[2]/h2/text()").extract()
        article['stats'] = response.xpath("//div[@class=author]/div[@class=articleGender]/text()").extract()
        article['content'] = response.xpath("//div[@class=content]/text()").extract()
        return article





