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

    class ReportItem(DjangoItem):
        django_model = ReportData
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

    class ReportItem(scrapy.Item):
        reptime = scrapy.Field()
        agency = scrapy.Field()
        reptype = scrapy.Field()
        lang = scrapy.Field()
        report = scrapy.Field()

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


