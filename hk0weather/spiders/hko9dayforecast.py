# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from hk0weather.items import ReportItem

class Hko9dayforecastSpider(Spider):
    name = "hko9dayforecast"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'http://www.weather.gov.hk/wxinfo/currwx/fndc.htm',
        'http://www.weather.gov.hk/wxinfo/currwx/fnd.htm',
        )

    def parse(self, response):
        sel = Selector(response)
        forecast = ReportItem()
        nineday = sel.xpath('//tr[@id="forecast_desc"]/td/div/text()').extract()
        for i in nineday:
          print(i)
        # wind direction and speed forecast
        # sel.xpath('//div[@id="fnd"]/table/tr').extract()[6]
