# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from RichardScrapy.items import BlogItem
import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")


class BlogSpider(Spider):
    name = "BlogSpider"
    # start_urls = [
    #     "http://blog.csdn.net/wuzhiguo1314"
    # ]

    def start_requests(self):
        for i in range(1,3):
            url = "http://blog.csdn.net/wuzhiguo1314/article/list/"+str(i)
            # self.start_urls.append(url)
            yield self.make_requests_from_url(url)

    def parse(self, response):


        # print response.body

        hxs = Selector(response)
        blogs = hxs.xpath("//div[@id='article_list']/div[@class='list_item article_item']")

        items = []

        for b in blogs:

            item = BlogItem()

            item['title'] = b.xpath("div/h1/span[@class='link_title']/a/text()").extract()
            item['link'] = b.xpath("div/h1/span[@class='link_title']/a/@href").extract()
            item['date'] = b.xpath("div[@class='article_manage']/span[@class='link_postdate']/text()").extract()

            items.append(item)
        # item['views'] = bolg.select("//<span[@class='link_view']/text()").extract()

        return items



    # '''
    # 字符串去空
    # '''
    # def stringTrip(self,content):
    #     return content.replace('\n', "").replace('\r', "").replace("<br/>", "").replace("　", "").strip()