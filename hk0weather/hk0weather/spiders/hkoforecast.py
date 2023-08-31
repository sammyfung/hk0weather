# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from hk0weather.items import ShortForecastItem
import json, re
from datetime import datetime


class HkoforecastSpider(Spider):
    '''
    HKOweather short term forecast open data
    https://data.gov.hk/en-data/dataset/hk-hko-rss-local-weather-forecast
    '''
    name = "hkoforecast"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en',
        'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc',
        )
    forecast = ShortForecastItem()

    def parse(self, response):
        self.forecast['scrape_time'] = datetime.now()
        data = json.loads(response.text)
        self.forecast['update_time'] = data['updateTime']
        if re.search('\&lang=en', response.url):
            self.forecast['general_en'] = data['generalSituation']
            self.forecast['period_en'] = data['forecastPeriod']
            self.forecast['forecast_en'] = data['forecastDesc']
            self.forecast['outlook_en'] = data['outlook']
        elif re.search('\&lang=tc', response.url):
            self.forecast['general_hk'] = data['generalSituation']
            self.forecast['period_hk'] = data['forecastPeriod']
            self.forecast['forecast_hk'] = data['forecastDesc']
            self.forecast['outlook_hk'] = data['outlook']
        try:
            assert len(self.forecast['general_en']) > 0
            assert len(self.forecast['general_hk']) > 0
            return self.forecast
        except KeyError:
            # ignore if any field is missing.
            pass
