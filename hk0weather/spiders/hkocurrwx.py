from scrapy.spider import Spider
from scrapy.selector import Selector
from hk0weather.items import HkocurrwxItem
import re

class HkocurrwxSpider(Spider):
    name = "hkocurrwx"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'http://www.weather.gov.hk/wxinfo/currwx/currentc.htm',
        )

    def parse(self, response):
        sel = Selector(response)
        currwx = HkocurrwxItem()
        line = sel.xpath('//div[@id="ming"]').extract()
        currwx['reptime'] = response.headers['Last-Modified']
        currwx['lang'] = "zh"
        for i in line:
          i = re.sub('<[^<]+?>', '', i)
          try:
            currwx['report'] += i
          except KeyError:
            currwx['report'] = i
        print currwx['report']
        return currwx
