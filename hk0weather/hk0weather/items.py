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
    rainfall = scrapy.Field()
    rainfall_unit = scrapy.Field()
    others = scrapy.Field()

class ForecastItem(scrapy.Item):
    crawler_name = scrapy.Field()
    data_provider_name = scrapy.Field()
    scraping_time = scrapy.Field()
    report_time = scrapy.Field()
    forecast_type = scrapy.Field()
    forecast_category = scrapy.Field()
    forecast_time = scrapy.Field()
    language = scrapy.Field()
    description = scrapy.Field()
    temperature_unit = scrapy.Field()
    temperature_max = scrapy.Field()
    temperature_min = scrapy.Field()
    humidity_max = scrapy.Field()
    humidity_min = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_speed = scrapy.Field()
    wind_max_gust = scrapy.Field()
    wind_speed_unit = scrapy.Field()
    wind_description = scrapy.Field()
    others = scrapy.Field()

