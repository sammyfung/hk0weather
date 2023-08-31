# -*- coding: utf-8 -*-
# Web Scraping for Hong Kong Observatory 10-minute update regional weather data.
import scrapy
from scrapy.selector import Selector
import logging
from hk0weather.items import RegionalItem
from hk0weather.hko import hko
import re, pytz
from datetime import datetime


class RegionalSpider(scrapy.Spider):
    name = "regional"
    allowed_domains = ["weather.gov.hk"]
    start_urls = (
        'http://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm',
    )

    def parse(self, response):
        laststation = ''
        temperture = int()
        stations = {}
        stationitems = []
        sel = Selector(response)
        report = sel.xpath('//pre[@id="ming"]/text()')

        # HKO report time.
        reptime = self.gettime(report[0].extract())

        for i in re.split('\n',report[0].extract()):
            laststation = ''
            station = {}
            hkobs = hko()
            for k,v in hko.cnameid:
                if re.sub(' ','',i[:6]) == k:
                    laststation = v
                    try:
                        station = stations[laststation]
                    except KeyError:
                        stations[laststation] = {}
                        stations[laststation]['scraptime'] = datetime.now(pytz.utc)
                        stations[laststation]['reptime'] = reptime
                        stations[laststation]['station'] = laststation
                        stations[laststation]['ename'] = hkobs.getename(laststation)
                        stations[laststation]['cname'] = hkobs.getcname(laststation)
            dataline = re.sub('^\s','',i[6:])
            dataline = re.sub('\*',' ',dataline)
            data = re.split('\s+',dataline)
            if len(data) > 5:
                for j in range(0,len(data)):
                    if data[j].isdigit():
                        #try:
                            stations[laststation]['humidity'] = int(data[j])
                        #except:
                        #    print(i)
                    elif laststation != '':
                        try:
                            if j == 1:
                                stations[laststation]['temperture'] = float(data[j])
                            elif j == 3:
                                stations[laststation]['temperturemax'] = float(data[j])
                            elif j == 5:
                                stations[laststation]['temperturemin'] = float(data[j])
                        except ValueError:
                            pass
                        except KeyError:
                            logging.warning("KeyError on Regional Weather Information: station %s, field %s"%(laststation,j))
            elif len(data) == 4 and laststation!='':
                # wind direction, wind speed, maximum gust.
                data[1] = re.sub(u'東南','Southeast', data[1])
                data[1] = re.sub(u'東北','Northeast', data[1])
                data[1] = re.sub(u'西南','Southwest', data[1])
                data[1] = re.sub(u'西北','Northwest', data[1])
                data[1] = re.sub(u'東','East', data[1])
                data[1] = re.sub(u'南','South', data[1])
                data[1] = re.sub(u'西','West', data[1])
                data[1] = re.sub(u'北','North', data[1])
                # 風向不定
                if not(re.search(u'^[A-Z].*',data[1])):
                    data[1] = 'Variable'
                stations[laststation]['winddirection'] = data[1]
                try:
                    stations[laststation]['windspeed'] = int(data[2])
                except ValueError:
                    pass
                try:
                    stations[laststation]['maxgust'] = int(data[3])
                except ValueError:
                    pass
            elif len(data) == 2:
                try:
                    stations[laststation]['pressure'] = float(data[1])
                except ValueError:
                    pass

        for key in stations:
            stationitem = RegionalItem()
            for key2 in stations[key]:
                stationitem[key2] = stations[key][key2]
            stationitems.append(stationitem)

        return stationitems

    def gettime(self, report):
        report = report.split('\n')
        for i in report:
            if re.search(u'錄得的天氣資料', i):
                t = re.sub(u'錄得的天氣資料.*','', i)
                t = re.sub(u' ','0', t)
                t = re.sub(u'[年月日時分]',' ', t)
                t = datetime.strptime(t,u'%Y %m %d %H %M ').replace(tzinfo = pytz.timezone('Etc/GMT-8'))
                return t

