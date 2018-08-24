# -*- coding: utf-8 -*-
import re

import scrapy
import time
from scrapy.spiders import Spider
from scrapy.selector import Selector
import sys

from tutorial.items import PunishItem

reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")


class BlogSpider(Spider):
    name = "YinJianJuPunishSpider"
    # start_urls = [
    #     "http://blog.csdn.net/wuzhiguo1314"
    # ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.YinJianJuPipeline': 1,
        }
    }

    def start_requests(self):
        # http://www.cbrc.gov.cn/zhuanti/xzcf/get2and3LevelXZCFDocListDividePage//1.html?current=1
        #获取1-3页的数据
        for i in range(1,10):
            url = "http://www.cbrc.gov.cn/zhuanti/xzcf/get2and3LevelXZCFDocListDividePage//1.html?current="+str(i)
            # self.start_urls.append(url)
            yield self.make_requests_from_url(url)


    def parse(self, response):

        #获取当页的数据
        urlList = response.xpath("//div[@class='xia3']//td[@class='cc']/a")
        for url in urlList:
            name = url.xpath("text()").extract()
            link = url.xpath("@href").extract()

            fullLink = response.urljoin(link[0])
            request = scrapy.Request(fullLink, callback=self.paseDetail)
            yield request
            # print str(name)+"=="+str(fullLink)

    def paseDetail(self,response):
        tab = response.xpath("//table[@class='MsoNormalTable']//td")

        title = response.xpath("//div[@id='docTitle']/div[@valign='top']/text()").extract()[0].strip()
        title = re.sub('[\r\n\t]', '', title).replace(" ","");
        link = response.url
        try:
            titleContent = title.split(":")
            pubDate = titleContent[1]
            source = titleContent[2]
            type = titleContent[3]

            pubDate = pubDate[0:pubDate.__len__()-4]
            source = source[0:source.__len__()-4]
        except Exception:
            print "title wrong"

        index = 0;
        for t in tab:
            content = t.xpath('string(.)').extract()[0].strip()
            if "处罚决定书文号" in content:
                index = tab.index(t)
                break;
        item = PunishItem()
        try:
            item['pubDate'] = pubDate
            item['source'] = source
            item['type'] = type
            item['link'] = link
            item['wenshuhao'] = tab[index+1].xpath('string(.)').extract()[0].strip()
            item['geren'] = tab[index+4].xpath('string(.)').extract()[0].strip()
            item['mingcheng'] = tab[index+7].xpath('string(.)').extract()[0].strip()
            item['fadingren'] = tab[index+9].xpath('string(.)').extract()[0].strip()
            item['weiguishishi'] = tab[index+11].xpath('string(.)').extract()[0].strip()
            item['chufayiju'] = tab[index+13].xpath('string(.)').extract()[0].strip()
            item['chufajueding'] = tab[index+15].xpath('string(.)').extract()[0].strip()
            item['jiguanmingcheng'] = tab[index+17].xpath('string(.)').extract()[0].strip()
            item['chufariqi'] = tab[index+19].xpath('string(.)').extract()[0].strip()
            yield item
        except Exception:
            print '数据格式不一致'
