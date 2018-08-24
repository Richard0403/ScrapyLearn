# -*- coding: utf-8 -*-
import sys
from scrapy import cmdline


# scrapy crawl field -o info.csv -t csv

#银监局
cmdline.execute("scrapy crawl YinJianJuPunishSpider".split())
#银监会机关
# cmdline.execute("scrapy crawl YinJianHuiJiGuanPunishSpider".split())
#银监会分局
# cmdline.execute("scrapy crawl YinJianFenJuPunishSpider".split())