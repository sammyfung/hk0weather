# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from hk0weather.items import ForecastItem
import json, re
from datetime import datetime


class Hko9dayforecastSpider(Spider):
    '''
    HKO 9-day weather forecast open data
    https://data.gov.hk/en-data/dataset/hk-hko-rss-9-day-weather-forecast
    '''
    name = "hko9dayforecast"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en',
        'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc',
        )
    days = []

    def parse(self, response):
        data = json.loads(response.text)
        for source in data['weatherForecast']:
            new_item = True
            item_num = len(self.days)
            target_item_num = -1
            forecast_date = datetime.strptime(source['forecastDate'], '%Y%m%d')
            for target in self.days:
                target_item_num += 1
                if target['date'] == forecast_date:
                    new_item = False
                    item_num = target_item_num
            if new_item:
                self.days.append(ForecastItem())
            self.days[item_num]['update_time'] = data['updateTime']
            self.days[item_num]['date'] = forecast_date
            self.days[item_num]['max_temp'] = source['forecastMaxtemp']['value']
            self.days[item_num]['min_temp'] = source['forecastMintemp']['value']
            self.days[item_num]['max_rh'] = source['forecastMaxrh']['value']
            self.days[item_num]['min_rh'] = source['forecastMinrh']['value']
            self.days[item_num]['icon'] = source['ForecastIcon']
            if re.search('\&lang=en', response.url):
                self.days[item_num]['general_en'] = data['generalSituation']
                self.days[item_num]['description_en'] = source['forecastWeather']
                self.days[item_num]['wind_en'] = source['forecastWind']
            elif re.search('\&lang=tc', response.url):
                self.days[item_num]['general_hk'] = data['generalSituation']
                self.days[item_num]['description_hk'] = source['forecastWeather']
                self.days[item_num]['wind_hk'] = source['forecastWind']
        try:
            for i in self.days:
                assert len(i['general_en']) > 0
                assert len(i['general_hk']) > 0
            return self.days
        except KeyError:
            # ignore if any field is missing.
            pass
