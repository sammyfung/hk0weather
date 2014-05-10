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
from stations import hko
import re, time

class CurrwxSpider(BaseSpider):
  name = "currwx"
  allowed_domains = ["weather.gov.hk"]
  start_urls = (
    'http://www.weather.gov.hk/textonly/current/rainfall_sr_uc.htm',
  )
 
  def parse(self, response):
    laststation = ''
    temperture = int()
    stations = []
    hxs = HtmlXPathSelector(response)
    report = hxs.select('//div[@id="ming"]')
    
    # HKO report time, temperture and humidity.
    time = self.gettime(report.extract()[0])
    o = self.hkocurrent(report.extract()[0])
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
        hkobs = hko()
        station['ename'] = hkobs.getename(laststation)
        station['cname'] = hkobs.getcname(laststation)
        station['temperture'] = temperture
        stations.append(station)
      else:
	for k,v in hko.cnameid:
          if re.sub(' ','',i)  == k:
            laststation = v
    return stations

  def gettime(self, report):
    report = report.split('\n')
    for i in report:
      if re.search(u'香 港 天 文 台.*報 告', i):
        if re.search(u'香 港 天 文 台 [0-9] .*報 告', i):
          repl = '0'
        else:
          repl = ''
        t = re.sub(u'.*香 港 天 文 台 在 ',repl,i)
        t = re.sub(u'發 出.*','',t)
        t = re.sub(u'上 午','AM',t)
        t = re.sub(u'下 午','PM',t)
        t = re.sub(u' ','',t)
        t = "%s "%time.localtime().tm_year + t
        t = time.strptime(t,u'%Y %m月%d日%p%I時%M分')
        t = time.mktime(t)
        return t

  def hkocurrent(self, report):
    report = re.sub(u'[ 。\r\n]','',report)
    report = re.sub(u'<br>','\n',report)
    report = report.split('\n')
    for i in report:
      if re.search(u'天文台錄得氣溫',i):
        c = {}
        c['temperture'] = re.sub(u'.*氣溫','',i)
        c['temperture'] = int(re.sub(u'度.*','',c['temperture']))
        c['humidity'] = int(re.sub(u'.*相對濕度百分之','',i))
        c['station'] = 'hko'
        return c

