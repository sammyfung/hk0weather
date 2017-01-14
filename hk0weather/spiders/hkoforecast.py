# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from hk0weather.items import ReportItem
from datetime import datetime
import re, pytz

class HkoforecastSpider(Spider):
    name = "hkoforecast"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'http://www.weather.gov.hk/wxinfo/currwx/flwc.htm',
        'http://www.weather.gov.hk/wxinfo/currwx/flw.htm',
        )

    def parse(self, response):
        sel = Selector(response)
        forecast = ReportItem()
        forecast['agency'] = 'HKO'
        forecast['reptype'] = 'forecast'
        forecast['reptime'] = datetime.strptime(response.headers['Last-Modified'].decode(encoding='UTF-8'),'%a, %d %b %Y %X %Z').replace(tzinfo = pytz.utc)
        if re.search('flwc.htm', response.url):
            forecast['lang'] = "zh_TW"
            forecast['report'] = sel.xpath('//span/text()').extract()[0]
            line = sel.xpath('//div[@id="ming"]').extract()
            for i in line:
                i = re.sub('<[^<]+?>', '', i)
                forecast['report'] += i
            forecast['report'] = re.sub('\t\t\t', '\r\n', forecast['report'])
        else:
            forecast['lang'] = "en"
            forecast['report'] = sel.xpath('//span/text()').extract()[0]
            # forecast['report'] += sel.xpath('//div').extract()[5]
            forecast['report'] += sel.xpath('//div')[25].xpath('div/div').extract()[0]
            forecast['report'] = re.sub('<br[^>]*>', '\r\n', forecast['report'])
            forecast['report'] = re.sub('<[^<]+?>', '', forecast['report'])
        return forecast
