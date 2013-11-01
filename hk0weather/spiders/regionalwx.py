#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       regionalwx.py
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
from hk0weather.items import Hk0RegionalItem
from hk0weather.libhk0.hk0 import hk0
import re

class RegionalwxSpider(BaseSpider):
  name = "regionalwx"
  allowed_domains = ["weather.gov.hk"]
  start_urls = (
    'http://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm',
  )
  stations = hk0.stations
 
  def parse(self, response):
    laststation = ''
    temperture = int()
    stations = []
    hxs = HtmlXPathSelector(response)
    report = hxs.select('//pre[@id="ming"]/text()')
    
    # HKO report time.
    time = hk0().gettime2(report[0].extract())

    for i in re.split('\n',report[0].extract()):
      laststation = ''
      station = Hk0RegionalItem()
      for k,v in self.stations:
        if re.sub(' ','',i[:5]) == k:
          laststation = v
          station['time'] = time
          station['station'] = laststation
      dataline = re.sub('^\s','',i[6:])
      dataline = re.sub('\*',' ',dataline)
      data = re.split('\s+',dataline)
      if len(data) >= 7:
        for j in range(0,len(data)):
          if data[j].isdigit():
            station['humidity'] = int(data[j])
          else:
            try:
              if j == 1:
                station['temperture'] = float(data[j])
              elif j == 3:
                station['temperturemax'] = float(data[j])
              elif j == 5:
                station['temperturemin'] = float(data[j])
            except ValueError:
              pass
        stations.append(station)
    return stations

