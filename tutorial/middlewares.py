# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from fake_useragent import UserAgent


class TutorialSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        exception_response = exception.response
        print 'process spider exception: ' + str(exception_response.status) + ', ' + exception_response.url
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TutorialDownloaderMiddleware(object):
    """This middleware enables working with sites that need cookies"""

    def process_request(self, request, spider):
        print 'Middleware process_request: ' + request.url
        return None

    def process_response(self, request, response, spider):
        print 'Middleware process_response: ' + response.url
        # print response.text
        return response


class RandomUserAgentMiddleware(object):
    # 随机更换user-agent
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        # self.ua = UserAgent()
        # self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        # def get_ua():
        #     return getattr(self.ua, self.ua_type)

        # request.headers.setdefault('User-Agent', get_ua())
        cookie = request.headers.get('Cookie')
        if cookie:
            print request.url + ', Cookie: ' + cookie
        else:
            user_agent_list = spider.crawler.settings.get('USER_AGENT_LIST', [])
            user_agent = random.choice(user_agent_list)
            request.headers['User-Agent'] = user_agent


class RandomProxyMiddleware(object):
    # 动态设置ip代理
    def process_request(self, request, spider):
        request.meta["proxy"] = ''
