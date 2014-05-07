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
from stations import hko
import re, time

class RegionalwxSpider(BaseSpider):
  name = "regionalwx"
  allowed_domains = ["weather.gov.hk"]
  start_urls = (
    'http://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm',
  )
 
  def parse(self, response):
    laststation = ''
    temperture = int()
    stations = {}
    stationitems = []
    hxs = HtmlXPathSelector(response)
    report = hxs.select('//pre[@id="ming"]/text()')
    
    # HKO report time.
    reptime = self.gettime(report[0].extract())

    for i in re.split('\n',report[0].extract()):
      laststation = ''
      station = {}
      hkobs = hko()
      for k,v in hko.cnameid:
        if re.sub(' ','',i[:5]) == k:
          laststation = v
          try:
            station = stations[laststation]
          except KeyError:
            stations[laststation] = {}
            stations[laststation]['scraptime'] = time.time()
            stations[laststation]['reptime'] = reptime
            stations[laststation]['station'] = laststation
            stations[laststation]['ename'] = hkobs.getename(laststation)
            stations[laststation]['cname'] = hkobs.getcname(laststation)
      dataline = re.sub('^\s','',i[6:])
      dataline = re.sub('\*',' ',dataline)
      data = re.split('\s+',dataline)
      #print "%s %s"%(len(data),data)
      if len(data) > 5:
        for j in range(0,len(data)):
          if data[j].isdigit():
            stations[laststation]['humidity'] = int(data[j])
          else:
            try:
              if j == 1:
                stations[laststation]['temperture'] = float(data[j])
              elif j == 3:
                stations[laststation]['temperturemax'] = float(data[j])
              elif j == 5:
                stations[laststation]['temperturemin'] = float(data[j])
            except ValueError:
              pass
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

    for key in stations:
      stationitem = Hk0RegionalItem()
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
        t = time.strptime(t,u'%Y年%m月%d日%H時%M分')
        t = int(time.mktime(t))
        return t

