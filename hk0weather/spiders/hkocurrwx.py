# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from hk0weather.items import ReportItem
from datetime import datetime
import re, pytz

class HkocurrwxSpider(Spider):
    name = "hkocurrwx"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'http://www.weather.gov.hk/wxinfo/currwx/currentc.htm',
        'http://www.weather.gov.hk/wxinfo/currwx/current.htm',
        )

    def parse(self, response):
        sel = Selector(response)
        currwx = ReportItem()
        currwx['agency'] = 'HKO'
        currwx['reptype'] = 'current'
        currwx['reptime'] = datetime.strptime(response.headers['Last-Modified'].decode(encoding='UTF-8'),'%a, %d %b %Y %X %Z').replace(tzinfo = pytz.utc)
        line = ''
        if re.search('currentc.htm', response.url): 
            currwx['lang'] = "zh_TW"
            line = sel.xpath('//div[@id="ming"]').extract()
            for i in line:
                i = re.sub('<[^<]+?>', '', i)
                try:
                    currwx['report'] += i
                except KeyError:
                    currwx['report'] = i
            currwx['report'] = re.sub('\r\n\r\n', '', currwx['report'])
        else:
            currwx['lang'] = "en"
            currwx['report'] = sel.xpath('//span/text()').extract()[0]
            # currwx['report'] += sel.xpath('//div').extract()[5]
            currwx['report'] += sel.xpath('//div')[25].xpath('div/div').extract()[0]
            currwx['report'] = re.sub('<br[^>]*>', '\r\n', currwx['report'])
            currwx['report'] = re.sub('</span>\r\n', '\t', currwx['report'])
            currwx['report'] = re.sub('<[^<]+?>', '', currwx['report'])
            currwx['report'] = re.sub('\r\n\r\n', '', currwx['report'])
        return currwx
