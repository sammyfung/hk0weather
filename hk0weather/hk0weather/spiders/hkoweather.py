# -*- coding: utf-8 -*-
# Web Scraping for Hong Kong weather data from Hong Kong Observatory
# - regional weather data updated by 10 minutes.
import scrapy
from scrapy.selector import Selector
import logging
from hk0weather.items import WeatherItem
import re
import pytz
import os
import json
from datetime import datetime


class HkoweatherSpider(scrapy.Spider):
    name = "hkoweather"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'https://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm',
        'https://www.weather.gov.hk/textonly/current/rainfall_sr.htm',
    )
    data_provider_name = 'HKO'
    sea_level_pressure_unit = 'hPa'
    temperature_unit = 'C'
    wind_speed_unit = 'kmh'
    rainfall_unit = 'mm'
    winds = (
        ('southeast', '東南'),
        ('northeast', '東北'),
        ('southwest', '西南'),
        ('northwest', '西北'),
        ('east', '東'),
        ('south', '南'),
        ('west', '西'),
        ('north', '北'),
        ('calm', '無風'),
        ('variable', '風向不定'),
    )
    hkt = pytz.timezone('Asia/Hong_Kong')

    def __init__(self, *args, **kwargs):
        super(HkoweatherSpider, self).__init__(*args, **kwargs)
        # Load JSON data from the specified file
        spider_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the JSON file
        json_stations_file = os.path.join(spider_dir, '../data/hko_stations.json')
        with open(json_stations_file, 'r', encoding='utf-8') as file:
            self.hko_stations = json.load(file)

        json_regions_file = os.path.join(spider_dir, '../data/hko_regions.json')
        with open(json_regions_file, 'r', encoding='utf-8') as file:
            self.hko_regions = json.load(file)

    def parse(self, response):
        if response.url == 'https://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm':
            items = self.parse_weather_info(response)
        elif response.url == 'https://www.weather.gov.hk/textonly/current/rainfall_sr.htm':
            items = self.parse_rainfall(response)
        else:
            items = None
        return items

    def parse_weather_info(self, response):
        stations = {}
        station_items = []
        sel = Selector(response)
        report = sel.xpath('//pre[@id="ming"]/text()')
        section = 'temperature'
        report_time = self.get_report_time(report[0].extract())

        for i in re.split('\n', report[0].extract()):
            # Identify section
            if re.search('風速及最高陣風風速', i):
                section = 'wind'
            elif re.search('平均海平面氣壓', i):
                section = 'pressure'
            elif re.search('十分鐘平均能見度', i):
                section = 'visibility'
            elif re.search('太陽總輻射量', i):
                section = 'solarradiation'
            station_code = self.get_station_code_by_name(re.sub(' ', '', i[:6]), lang='chinese_name')
            if station_code:
                try:
                    station = stations[station_code]
                except KeyError:
                    stations[station_code] = {}
                    stations[station_code]['crawler_name'] = self.name
                    stations[station_code]['data_provider_name'] = self.data_provider_name
                    stations[station_code]['scraping_time'] = datetime.now(self.hkt).isoformat(timespec='milliseconds')
                    stations[station_code]['report_time'] = report_time.isoformat(timespec='milliseconds')
                    stations[station_code]['station_code'] = station_code
                    stations[station_code]['station_name'] = self.hko_stations[station_code]['english_name']
                    stations[station_code]['station_name_hk'] = self.hko_stations[station_code]['chinese_name']
                    stations[station_code]['others'] = dict()
            else:
                continue

            dataline = re.sub('^ *[^ ]', '', i[6:])
            dataline = re.sub('\t', '    ', i[6:])
            dataline = re.sub(' +', ',', dataline)
            data = re.split(',', dataline)

            # Handling sections
            if section == 'temperature' and station_code != '':
                # Temperature section
                stations[station_code]['temperature_unit'] = self.temperature_unit
                for j in range(0, len(data)):
                    if data[j].isdigit():
                        stations[station_code]['humidity'] = int(data[j])
                    elif station_code != '':
                        try:
                            if j == 1:
                                stations[station_code]['temperature'] = float(data[j])
                            elif j == 3:
                                stations[station_code]['temperature_max'] = float(data[j])
                            elif j == 5:
                                stations[station_code]['temperature_min'] = float(data[j])
                            elif j == 6:
                                stations[station_code]['others']['temperature_past_24hr_difference'] = float(data[j])
                            elif j == 7:
                                stations[station_code]['others']['temperature_grass'] = float(data[j])
                            elif j == 8:
                                stations[station_code]['others']['temperature_grass_min'] = float(data[j])
                        except ValueError:
                            pass
                        except KeyError:
                            logging.warning(f"KeyError on Regional Weather Information: station {station_code}, field {j}")
            elif section == 'wind' and station_code != '':
                stations[station_code]['wind_direction'] = ''
                stations[station_code]['wind_speed_unit'] = self.wind_speed_unit
                for (wind_k, wind_v) in self.winds:
                    stations[station_code]['wind_direction'] = wind_k if data[1] == wind_v else stations[station_code]['wind_direction']
                if stations[station_code]['wind_direction'] != 'calm':
                    try:
                        stations[station_code]['wind_speed'] = int(data[2])
                    except ValueError:
                        pass
                try:
                    stations[station_code]['wind_max_gust'] = int(data[3])
                except ValueError:
                    pass
            elif section == 'pressure' and station_code != '':
                # Sea Level Pressure section
                stations[station_code]['sea_level_pressure_unit'] = self.sea_level_pressure_unit
                try:
                    stations[station_code]['sea_level_pressure'] = float(data[1])
                except ValueError:
                    pass
                except IndexError:
                    pass
            elif section == 'visibility' and station_code != '':
                # 10-Minute Mean Visibility
                if data[2] == '公里':
                    stations[station_code]['visibility_unit'] = 'km'
                elif data[2] == '米':
                    stations[station_code]['visibility_unit'] = 'm'
                try:
                    stations[station_code]['visibility_distance'] = int(data[1])
                except ValueError:
                    if re.search('N/A', data[1]):
                        stations[station_code]['others']['missing_reason_visibility_distance'] = 'N/A'

        for key in stations:
            station_item = WeatherItem()
            for key2 in stations[key]:
                if key2 != 'others':
                    station_item[key2] = stations[key][key2]
                elif stations[key][key2] != {}:
                    station_item[key2] = json.dumps(stations[key][key2])
            station_items.append(station_item)

        return station_items

    def parse_rainfall(self, response):
        region_items = []
        sel = Selector(response)
        reptime = sel.xpath('//span/text()')[0].extract()
        region_name = sel.xpath('//tr/td[contains(@style,"width:200px;")]/text()').extract()
        rainfall_raw_data = sel.xpath('//tr/td[contains(@style,"width:90px;")]/text()').extract()

        for i in range(0, len(region_name)):
            region_item = WeatherItem()
            region_item['crawler_name'] = self.name
            region_item['data_provider_name'] = self.data_provider_name
            region_item['scraping_time'] = datetime.now(self.hkt).isoformat(timespec='milliseconds')
            region_item['rainfall_unit'] = self.rainfall_unit
            region_item['report_time'] = self.get_report_time_rainfall(reptime)
            region_item['station_code'] = self.get_region_code_by_name(region_name[i])
            region_item['station_name'] = self.hko_regions[region_item['station_code']]['english_name']
            region_item['station_name_hk'] = self.hko_regions[region_item['station_code']]['chinese_name']
            region_item['rainfall'] = rainfall_raw_data[i]
            others = dict()
            if re.search(" to ", rainfall_raw_data[i]):
                rainfall_data = re.split(" to ", re.sub(f' {self.rainfall_unit}', '', rainfall_raw_data[i]))
                try:
                    region_item['rainfall'] = int(rainfall_data[1])
                    others['rainfall_hourly_min'] = int(rainfall_data[0])
                    others['rainfall_hourly_max'] = int(rainfall_data[1])
                except IndexError:
                    others = dict()
                    others['rainfall_hourly_raw_data'] = rainfall_raw_data[i]
            else:
                rainfall_data = re.sub(f' {self.rainfall_unit}', '', rainfall_raw_data[i])
                region_item['rainfall'] = int(rainfall_data)
                others['rainfall_hourly_raw_data'] = rainfall_raw_data[i]
            region_item['others'] = json.dumps(others)
            region_items.append(region_item)
        return region_items

    def get_report_time(self, report):
        report = report.split('\n')
        for i in report:
            if re.search('錄得的天氣資料', i):
                t = re.sub('錄得的天氣資料.*', '', i)
                t = re.sub(' ', '0', t)
                t = re.sub('[年月日時分]', ' ', t)
                t = datetime.strptime(t, '%Y %m %d %H %M ').replace(tzinfo=pytz.timezone('Etc/GMT-8'))
                return t

    def get_report_time_rainfall(self, timeperiod):
        endtime = re.sub('^.* and ', '',timeperiod)
        endtime = re.sub(',.*', '',endtime)
        endtime = re.sub('\\.', '',endtime).upper()
        endtime = re.sub('^0', '12',endtime)
        endtime = datetime.combine(datetime.today().date(), datetime.strptime(endtime, "%I:%M %p").time())
        endtime = endtime.replace(tzinfo=pytz.timezone('Etc/GMT-8')).isoformat(timespec='milliseconds')
        return endtime

    def get_station_code_by_name(self, station_name, lang='english_name'):
        for key, value in self.hko_stations.items():
            if value[lang] == station_name:
                return key
        return None

    def get_region_code_by_name(self, region_name, lang='english_name'):
        for key, value in self.hko_regions.items():
            if value[lang] == region_name:
                return key
        return None
