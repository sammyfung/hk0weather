# -*- coding: utf-8 -*-
import scrapy

class WeatherItem(scrapy.Item):
    crawler_name = scrapy.Field()
    data_provider_name = scrapy.Field()
    scraping_time = scrapy.Field()
    report_time = scrapy.Field()
    station_code = scrapy.Field()
    station_name = scrapy.Field()
    station_name_hk = scrapy.Field()
    temperature = scrapy.Field()
    temperature_unit = scrapy.Field()
    temperature_max = scrapy.Field()
    temperature_min = scrapy.Field()
    humidity = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_speed = scrapy.Field()
    wind_max_gust = scrapy.Field()
    wind_speed_unit = scrapy.Field()
    sea_level_pressure = scrapy.Field()
    sea_level_pressure_unit = scrapy.Field()
    visibility_distance = scrapy.Field()
    visibility_unit = scrapy.Field()

class RainfallItem(scrapy.Item):
    scraptime = scrapy.Field()
    reptime = scrapy.Field()
    ename = scrapy.Field()
    cname = scrapy.Field()
    rainfallmin = scrapy.Field()
    rainfallmax = scrapy.Field()

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

