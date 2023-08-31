# -*- coding: utf-8 -*-
# Web Scraping for Hong Kong Rainfall data of past hour.
import scrapy
from scrapy.selector import Selector
from hk0weather.items import RainfallItem
import re, pytz
from datetime import datetime


class RainfallSpider(scrapy.Spider):
    name = "rainfall"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'http://www.weather.gov.hk/textonly/current/rainfall_sr.htm',
    )
    cname = {'Southern District': u'南區',
        'Islands District': u'離島區',
        'Wan Chai': u'灣仔',
        'Central & Western District': u'中西區',
        'Kwun Tong': u'觀塘',
        'Eastern District': u'東區',
        'Sai Kung': u'西貢',
        'Yau Tsim Mong': u'油尖旺',
        'Kowloon City': u'九龍城',
        'Wong Tai Sin': u'黃大仙',
        'Sha Tin': u'沙田',
        'Tai Po': u'大埔',
        'Sham Shui Po': u'深水埗',
        'Kwai Tsing': u'葵青',
        'Tsuen Wan': u'荃灣',
        'Tuen Mun': u'屯門',
        'North District': u'北區',
        'Yuen Long': u'元朗'}

    def parse(self, response):
        stationitems = []
        sel = Selector(response)
        reptime = sel.xpath('//span/text()')[0].extract()
        report = sel.xpath('//tr/td[contains(@style,"width:200px;")]/text()').extract()
        for i in range(0,len(report)):
            stationitem = RainfallItem()
            stationitem['scraptime'] = datetime.now(pytz.utc)
            stationitem['reptime'] = self.parse_time(reptime)
            stationitem['ename'] = report[i]
            try:
                stationitem['cname'] = self.cname[report[i]]
            except KeyError:
                pass
            rainfall = sel.xpath('//tr/td[contains(@style,"width:90px;")]/text()')[i].extract()
            rainfall = re.split(" to ", re.sub(' mm','',rainfall))
            stationitem['rainfallmin'] = rainfall[0]
            stationitem['rainfallmax'] = rainfall[1]
            stationitems.append(stationitem)
        return stationitems

    def parse_time(self, timeperiod):
        endtime = re.sub('^.* and ','',timeperiod)
        endtime = re.sub(',.*','',endtime)
        endtime = re.sub('\.','',endtime).upper()
        endtime = re.sub('^0','12',endtime)
        endtime = datetime.combine(datetime.today().date(), datetime.strptime(endtime,"%I:%M %p").time())
        endtime = endtime.replace(tzinfo = pytz.timezone('Etc/GMT-8'))
        return endtime
