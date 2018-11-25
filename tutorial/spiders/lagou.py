# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']
    custom_settings = {
        # cookie 自动传递 默认 False
        'COOKIES_ENABLED': False,
        # cookie debug日志打印 默认 False
        'COOKIES_DEBUG': True,

        # downloader 并发请求(concurrent requests)的最大值 默认32 会导致拉勾反爬虫 提示登录重定向
        'CONCURRENT_REQUESTS': 1,
        # downloader 在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力
        'DOWNLOAD_DELAY': 5,

        # 默认情况下， RFPDupeFilter 只记录第一次重复的请求。 设置 DUPEFILTER_DEBUG 为 True 将会使其记录所有重复的requests
        'DUPEFILTER_DEBUG': True,
    }

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.+'), callback='parse_zhaopin', follow=True),
        Rule(LinkExtractor(allow=r'gongsi/j\d+.html'), callback='parse_gongsi', follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_jobs', follow=True)
    )

    def parse_start_url(self, response):
        return []

    def process_results(self, response, results):
        return results

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def parse_zhaopin(self, response):
        i = {}
        self.print_info(response, 'zhaopin')
        return i

    def parse_gongsi(self, response):
        i = {}
        self.print_info(response, 'gongsi')
        return i

    def parse_jobs(self, response):
        i = {}
        self.print_info(response, 'jobs')
        return i

    def print_info(self, response, title):
        print title + ' response successfully, ' + response.url + ', depth: ' + str(
            response.meta['depth']) + ', referer: ' + response.request.headers['Referer']
