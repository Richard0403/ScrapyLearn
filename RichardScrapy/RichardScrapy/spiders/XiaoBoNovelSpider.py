# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.spiders import Spider
from scrapy.selector import Selector
from RichardScrapy.items import BlogItem, FileItem, NovelItem
import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")


class BlogSpider(Spider):
    name = "XiaoBoNovelSpider"
    # start_urls = [
    #     "http://blog.csdn.net/wuzhiguo1314"
    # ]

    def start_requests(self):
        yield self.make_requests_from_url("http://www.henca888.com/html/part/index31.html")
        for i in range(2,69):
            url = "http://www.henca888.com/html/part/index31_"+str(i)+".html"
            # self.start_urls.append(url)
            yield self.make_requests_from_url(url)


    def parse(self, response):

        urlList = response.xpath("//ul[@class='textList']/li")

        items = []

        for url in urlList:
            name = url.xpath("a/text()").extract()
            link = url.xpath("a/@href").extract()

            fullLink = response.urljoin(link[0])
            # print fullLink
            request = scrapy.Request(fullLink, callback=self.paseDetail)
            yield request;
            # print str(name)+"=="+str(link)

    def paseDetail(self,response):
        novel = response.xpath("//div[@class='novelContent']").extract()
        name = response.xpath("//p[@align='center']/font").extract()


        novelItem = NovelItem()
        novelItem['name'] = name
        novelItem['content'] = novel
        novelItem['createTime'] = time.time()

        yield novelItem

        # print novel
