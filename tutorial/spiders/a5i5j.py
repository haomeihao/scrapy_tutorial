# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request


class A5i5jSpider(scrapy.Spider):
    name = '5i5j'
    allowed_domains = ['bj.5i5j.com']
    start_urls = ['https://bj.5i5j.com/ershoufang/']

    custom_settings = {
        # cookie 自动传递 默认False 会自动处理js跳转问题 重定向问题
        'COOKIES_ENABLED': True,
        # cookie debug日志打印 默认False
        'COOKIES_DEBUG': True,

        # downloader 并发请求(concurrent requests)的最大值 默认32 会导致拉勾反爬虫 提示登录重定向
        'CONCURRENT_REQUESTS': 1,
        # downloader 在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力
        'DOWNLOAD_DELAY': 5,

        # 默认情况下， RFPDupeFilter 只记录第一次重复的请求。 设置 DUPEFILTER_DEBUG 为 True 将会使其记录所有重复的requests
        'DUPEFILTER_DEBUG': True,
    }

    def parse(self, response):
        self.print_info(response, 'parse')
        for url in self.start_urls:
            yield Request(url=url, callback=self.sub_parse)

    def sub_parse(self, response):
        self.print_info(response, 'sub_parse')
        for url in self.start_urls:
            yield Request(url=url, callback=self.sub_parse)

    def print_info(self, response, title):
        print title + ' response, status: ' + str(response.status) + ', url: ' + response.url + ', depth: ' + str(
            response.meta.get('depth', 0)) + ', referer: ' + response.request.headers.get('Referer', 'None')
        print response.text
