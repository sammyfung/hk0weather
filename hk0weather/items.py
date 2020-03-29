# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

try:
    from scrapy_djangoitem import DjangoItem
    from openweather.models import WeatherData, RainfallData, ReportData

    class RegionalItem(DjangoItem):
        django_model = WeatherData

    class RainfallItem(DjangoItem):
        django_model = RainfallData
except ImportError:
    import scrapy

    class RegionalItem(scrapy.Item):
        scraptime = scrapy.Field()
        reptime = scrapy.Field()
        station = scrapy.Field()
        ename = scrapy.Field()
        cname = scrapy.Field()
        temperture = scrapy.Field()
        humidity = scrapy.Field()
        temperturemax = scrapy.Field()
        temperturemin = scrapy.Field()
        winddirection = scrapy.Field()
        windspeed = scrapy.Field()
        maxgust = scrapy.Field()
        pressure = scrapy.Field()

    class RainfallItem(scrapy.Item):
        scraptime = scrapy.Field()
        reptime = scrapy.Field()
        ename = scrapy.Field()
        cname = scrapy.Field()
        rainfallmin = scrapy.Field()
        rainfallmax = scrapy.Field()

    class Hk0WeatherItem(scrapy.Item):
        time = scrapy.Field()
        station = scrapy.Field()
        ename = scrapy.Field()
        cname = scrapy.Field()
        temperture = scrapy.Field()
        humidity = scrapy.Field()

    class Hk0TropicalItem(scrapy.Item):
        time = scrapy.Field()
        postime = scrapy.Field()
        x = scrapy.Field()
        y = scrapy.Field()
        category = scrapy.Field()
        windspeed = scrapy.Field()
        tctype = scrapy.Field()


class ForecastItem(scrapy.Item):
    update_time = scrapy.Field()
    date = scrapy.Field()
    general_en = scrapy.Field()
    general_hk = scrapy.Field()
    description_en = scrapy.Field()
    description_hk = scrapy.Field()
    wind_en = scrapy.Field()
    wind_hk  = scrapy.Field()
    max_temp = scrapy.Field()
    min_temp = scrapy.Field()
    max_rh = scrapy.Field()
    min_rh = scrapy.Field()
    icon = scrapy.Field()


class ShortForecastItem(scrapy.Item):
    scrape_time = scrapy.Field()
    update_time = scrapy.Field()
    general_en = scrapy.Field()
    general_hk = scrapy.Field()
    period_en = scrapy.Field()
    period_hk = scrapy.Field()
    forecast_en = scrapy.Field()
    forecast_hk = scrapy.Field()
    outlook_en = scrapy.Field()
    outlook_hk = scrapy.Field()

