# -*- coding: utf-8 -*-

from scrapy import Spider
import json
from scrapy.http import Request
from RichardScrapy.items import NeihanItem

class NeihanSpider(Spider):
    flag = 0;
    name = "Neihan"
    allowed_domains = ["snssdk.com"]
    start_urls = [
        "http://ic.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-102&message_cursor=-1&longitude=116.62438757667&latitude=39.931386268666&bd_longitude=116.611834&bd_latitude=39.928882&bd_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_longitude=116.611803&am_latitude=39.928944&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1463541146157&count=30&min_time=1463540965&screen_width=1080&iid=4074681484&device_id=13831748938&ac=wifi&channel=lephone&aid=7&app_name=joke_essay&version_code=500&version_name=5.0.0&device_platform=android&ssmix=a&device_type=ZUK+Z1&os_api=23&os_version=6.0.1&uuid=867695020560495&openudid=1fa8cdd99ae22c08&manifest_version_code=500",
        "http://ic.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-102&message_cursor=-1&longitude=116.62438757667&latitude=39.931386268666&bd_longitude=116.611834&bd_latitude=39.928882&bd_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_longitude=116.611803&am_latitude=39.928944&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1463541146157&count=30&min_time=1463540965&screen_width=1080&iid=4074681484&device_id=13831748938&ac=wifi&channel=lephone&aid=7&app_name=joke_essay&version_code=500&version_name=5.0.0&device_platform=android&ssmix=a&device_type=ZUK+Z1&os_api=23&os_version=6.0.1&uuid=867695020560495&openudid=1fa8cdd99ae22c08&manifest_version_code=500",
        # 'http://www.baidu.com',
        # 'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        # 'http://www.douban.com/group/explore?tag=%E8%B4%AD%E7%89%A9'
    ]


    def parse(self, response):
        print "=="
        self.flag+=1
        url = 'http://ic.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1&content_type=-102&message_cursor=-1&longitude=116.62438'+str(self.flag)+'757667&latitude=39.931386268666&bd_longitude=116.611834&bd_latitude=39.928882&bd_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_longitude=116.611803&am_latitude=39.928944&am_city=%E5%8C%97%E4%BA%AC%E5%B8%82&am_loc_time=1463541146157&count=30&min_time=1463540965&screen_width=1080&iid=4074681484&device_id=13831748938&ac=wifi&channel=lephone&aid=7&app_name=joke_essay&version_code=500&version_name=5.0.0&device_platform=android&ssmix=a&device_type=ZUK+Z1&os_api=23&os_version=6.0.1&uuid=867695020560495&openudid=1fa8cdd99ae22c08&manifest_version_code=500'
        # self.make_requests_from_url(url).replace(callback=self.parse)
        yield Request(url, callback= self.parse)

        dic = json.loads(response.body)

        listdata = dic['data']['data']
        print dic['message']
        items = []
        for i_data in listdata:
            if(i_data.has_key('group')):
                #消息内容
                content = i_data['group']['content']
                #消息id
                mId = i_data['group']['id']
                #用户id
                uId = i_data['group']['user']['user_id']
                #用户名
                uName = i_data['group']['user']['name']
                #用户头像
                uIcon = i_data['group']['user']['avatar_url']

                item = NeihanItem()
                # item.content = content
                item['content'] = content
                item['uName'] = uName
                item['mId'] = mId
                item['uId'] = uId
                item['uIcon'] = uIcon

                yield item
                items.append(item)
