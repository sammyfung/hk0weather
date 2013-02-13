#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       currex.py
#       
#       Copyright 2013 Sammy Fung <sammy@sammy.hk>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hk0weather.items import Hk0WeatherItem
from hk0weather.libhk0.hk0 import hk0

class CurrwxSpider(BaseSpider):
  name = "currwx"
  allowed_domains = ["weather.gov.hk"]
  start_urls = (
    'http://www.weather.gov.hk/wxinfo/currwx/currentc.htm',
  )
  stations = hk0.stations
 
  def parse(self, response):
    laststation = ''
    temperture = int()
    stations = []
    hxs = HtmlXPathSelector(response)
    report = hxs.select('//div[@id="ming"]')
    
    # HKO report time, temperture and humidity.
    time = hk0().gettime(report.extract()[0])
    o = hk0().hk0current(report.extract()[0])
    station = Hk0WeatherItem()
    station['time'] = int(time)
    station['station'] = o['station']
    station['temperture'] = o['temperture']
    station['humidity'] = o['humidity']
    stations.append(station)

    # Other regional air temperatures.
    for i in report.select('span/text()').extract():
      if i.isdigit():
        temperture = int(i)
        station = Hk0WeatherItem()
        station['time'] = int(time)
        station['station'] = laststation
        station['temperture'] = temperture
        stations.append(station)
      else:
	for k,v in self.stations:
          if i == k:
            laststation = v
    return stations

