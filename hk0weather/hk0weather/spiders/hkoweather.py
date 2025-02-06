# -*- coding: utf-8 -*-
# Web Scraping for Hong Kong weather data from Hong Kong Observatory
# - regional weather data updated by 10 minutes.
import scrapy
from scrapy.selector import Selector
import logging
from hk0weather.items import WeatherItem
import re, pytz, os, json
from datetime import datetime


class HkoweatherSpider(scrapy.Spider):
    name = "hkoweather"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'https://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm',
    )
    data_provider_name = 'HKO'
    sea_level_pressure_unit = 'hPa'
    temperature_unit = 'C'
    visibility_unit = 'km'
    wind_speed_unit = 'kmh'

    def __init__(self, *args, **kwargs):
        super(HkoweatherSpider, self).__init__(*args, **kwargs)
        # Load JSON data from the specified file
        spider_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the JSON file
        json_file = os.path.join(spider_dir, '../data/hko_stations.json')
        with open(json_file, 'r', encoding='utf-8') as file:
            self.hko_stations = json.load(file)

    def parse(self, response):
        if response.url == 'https://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm':
            items = self.parse_weather_info(response)
        else:
            items = None
        return items

    def parse_weather_info(self, response):
        stations = {}
        station_items = []
        sel = Selector(response)
        report = sel.xpath('//pre[@id="ming"]/text()')
        hkt = pytz.timezone('Asia/Hong_Kong')
        section = 'temperature'
        report_time = self.get_report_time(report[0].extract())

        for i in re.split('\n',report[0].extract()):
            # Identify section
            if re.search('風速及最高陣風風速', i):
                section = 'wind'
            elif re.search('平均海平面氣壓', i):
                section = 'pressure'
            elif re.search('十分鐘平均能見度', i):
                section = 'visibility'
            elif re.search('太陽總輻射量', i):
                section = 'solarradiation'
            laststation = self.get_code_by_name(re.sub(' ','',i[:6]), lang='chinese_name')
            if laststation:
                try:
                    station = stations[laststation]
                except KeyError:
                    stations[laststation] = {}
                    stations[laststation]['crawler_name'] = self.name
                    stations[laststation]['data_provider_name'] = self.data_provider_name
                    stations[laststation]['scraping_time'] = datetime.now(hkt).isoformat(timespec='milliseconds')
                    stations[laststation]['report_time'] = report_time.isoformat(timespec='milliseconds')
                    stations[laststation]['station_code'] = laststation
                    stations[laststation]['station_name'] = self.hko_stations[laststation]['english_name']
                    stations[laststation]['station_name_hk'] = self.hko_stations[laststation]['chinese_name']
            else:
                continue

            dataline = re.sub('^ ','',i[6:])
            dataline = re.sub('\\*',' ',dataline)
            data = re.split(' +',dataline)

            # Handling sections
            if section == 'temperature' and laststation != '':
                # Temperature section
                stations[laststation]['temperature_unit'] = self.temperature_unit
                for j in range(0,len(data)):
                    if data[j].isdigit():
                        #try:
                            stations[laststation]['humidity'] = int(data[j])
                        #except:
                        #    print(i)
                    elif laststation != '':
                        try:
                            if j == 1:
                                stations[laststation]['temperature'] = float(data[j])
                            elif j == 3:
                                stations[laststation]['temperature_max'] = float(data[j])
                            elif j == 5:
                                stations[laststation]['temperature_min'] = float(data[j])
                        except ValueError:
                            pass
                        except KeyError:
                            logging.warning("KeyError on Regional Weather Information: station %s, field %s"%(laststation,j))
            elif section == 'wind' and laststation != '':
                # Wind section - wind direction, speed, and maximum gust.
                stations[laststation]['wind_speed_unit'] = self.wind_speed_unit
                # Wind direction
                data[1] = re.sub('東南','southeast', data[1])
                data[1] = re.sub('東北','northeast', data[1])
                data[1] = re.sub('西南','southwest', data[1])
                data[1] = re.sub('西北','northwest', data[1])
                data[1] = re.sub('東','east', data[1])
                data[1] = re.sub('南','south', data[1])
                data[1] = re.sub('西','west', data[1])
                data[1] = re.sub('北','north', data[1])
                if not(re.search('^[a-z].*',data[1])):
                    # Variable wind direction
                    data[1] = 'variable'
                stations[laststation]['wind_direction'] = data[1]
                # Wind Speed
                try:
                    stations[laststation]['wind_speed'] = int(data[2])
                except ValueError:
                    pass
                # Max Gust
                try:
                    stations[laststation]['wind_max_gust'] = int(data[3])
                except ValueError:
                    pass
            elif section == 'pressure' and laststation != '':
                # Sea Level Pressure section
                stations[laststation]['sea_level_pressure_unit'] = self.sea_level_pressure_unit
                try:
                    stations[laststation]['sea_level_pressure'] = float(data[1])
                except ValueError:
                    stations[laststation]['sea_level_pressure'] = float(data[0])
                except IndexError:
                    print(data)
            elif section == 'visibility' and laststation != '':
                # 10-Minute Mean Visibility
                stations[laststation]['visibility_unit'] = self.visibility_unit
                try:
                    stations[laststation]['visibility_distance'] = int(data[1])
                except ValueError:
                    stations[laststation]['visibility_distance'] = data
                    pass
                except IndexError:
                    print(data)

        for key in stations:
            station_item = WeatherItem()
            for key2 in stations[key]:
                station_item[key2] = stations[key][key2]
            station_items.append(station_item)

        return station_items

    def get_report_time(self, report):
        report = report.split('\n')
        for i in report:
            if re.search('錄得的天氣資料', i):
                t = re.sub('錄得的天氣資料.*','', i)
                t = re.sub(' ','0', t)
                t = re.sub('[年月日時分]',' ', t)
                t = datetime.strptime(t, '%Y %m %d %H %M ').replace(tzinfo = pytz.timezone('Etc/GMT-8'))
                return t

    def get_code_by_name(self, station_name, lang='english_name'):
        for key, value in self.hko_stations.items():
            if value[lang] == station_name:
                return key
        return None