# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from hk0weather.items import ForecastItem
import json, re, pytz
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
        'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=en',
        'https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc',
        )
    data_provider_name = 'HKO'
    sea_level_pressure_unit = 'hPa'
    temperature_unit = 'C'
    visibility_unit = 'km'
    wind_speed_unit = 'kmh'
    #forecast = ShortForecastItem()

    def parse(self, response):
        self.hkt = pytz.timezone('Asia/Hong_Kong')
        if re.search('dataType=flw', response.url):
            items = self.parse_hko_forecast(response)
        elif re.search('dataType=fnd', response.url):
            items = self.parse_hko_9day_forecast(response)
        else:
            items = None
        return items

    def parse_hko_forecast(self, response):
        data = json.loads(response.text)
        items = []
        item = ForecastItem()
        item['crawler_name'] = self.name
        item['data_provider_name'] = self.data_provider_name
        item['scraping_time'] = datetime.now(self.hkt).isoformat(timespec='milliseconds')
        update_time = datetime.fromisoformat(data['updateTime']).isoformat(timespec='milliseconds')
        item['report_time'] = update_time
        item['forecast_type'] = 'forecast'
        item['forecast_time'] = update_time
        item['others'] = {'forecast_period': data['forecastPeriod']}
        item['language'] = 'en'
        forecast_item = ForecastItem()
        forecast_item.update(item)
        outlook_item = ForecastItem()
        outlook_item.update(item)

        if re.search('&lang=en', response.url):
            item['forecast_category'] = 'general_situation'
            item['description'] = data['generalSituation']
            forecast_item['forecast_category'] = 'forecast'
            forecast_item['description'] = data['forecastDesc']
            outlook_item['forecast_category'] = 'outlook'
            outlook_item['description'] = data['outlook']
        elif re.search('&lang=tc', response.url):
            language = 'zh_hk'
            item['language'] = language
            item['forecast_category'] = 'general_situation'
            item['description'] = data['generalSituation']
            forecast_item['language'] = language
            forecast_item['forecast_category'] = 'forecast'
            forecast_item['description'] = data['forecastDesc']
            outlook_item['language'] = language
            outlook_item['forecast_category'] = 'outlook'
            outlook_item['description'] = data['outlook']

        items.append(item)
        items.append(forecast_item)
        items.append(outlook_item)
        return items

    def parse_hko_9day_forecast(self, response):
        data = json.loads(response.text)
        items = []
        item = ForecastItem()
        item['crawler_name'] = self.name
        item['data_provider_name'] = self.data_provider_name
        item['scraping_time'] = datetime.now(self.hkt).isoformat(timespec='milliseconds')
        item['report_time'] = datetime.fromisoformat(data['updateTime']).isoformat(timespec='milliseconds')
        item['forecast_type'] = 'forecast_9day'
        item['language'] = 'en'
        if re.search('&lang=en', response.url):
            item['language'] = 'en'
        elif re.search('&lang=tc', response.url):
            item['language'] = 'zh_hk'

        first_forecast_date = None
        general_item = ForecastItem()
        general_item.update(item)
        general_item['forecast_category'] = 'general_situation'
        general_item['description'] = data['generalSituation']

        for source in data['weatherForecast']:
            is_new_item = True
            item_num = len(items)
            target_item_num = -1
            naive_datetime = datetime.strptime(source['forecastDate'], '%Y%m%d')
            localized_datetime = self.hkt.localize(naive_datetime)
            forecast_date = localized_datetime.isoformat(timespec='milliseconds')
            first_forecast_date = forecast_date if not first_forecast_date else first_forecast_date
            for target in items:
                target_item_num += 1
                if target['forecast_time'] == forecast_date:
                    is_new_item = False
                    item_num = target_item_num
            if is_new_item:
                new_item = ForecastItem()
                new_item.update(item)
                items.append(new_item)
            items[item_num]['temperature_unit'] = self.temperature_unit
            items[item_num]['forecast_time'] = forecast_date
            items[item_num]['forecast_category'] = 'daily'
            items[item_num]['temperature_max'] = source['forecastMaxtemp']['value']
            items[item_num]['temperature_min'] = source['forecastMintemp']['value']
            items[item_num]['humidity_max'] = source['forecastMaxrh']['value']
            items[item_num]['humidity_min'] = source['forecastMinrh']['value']
            forecast_icon = source['ForecastIcon']
            general_situation = data['generalSituation']
            items[item_num]['description'] = source['forecastWeather']
            items[item_num]['wind_description'] = source['forecastWind']
            items[item_num]['others'] = {
                'forecast_icon': forecast_icon,
            }

        general_item['forecast_time'] = first_forecast_date
        items.append(general_item)
        return items
