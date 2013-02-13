#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       hk0.py
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

import re, time

class hk0:
  stations = [
    (u'天 文 台 ', 'hko'),
    (u'京 士 柏 ', 'kingspark'),
    (u'黃 竹 坑 ', 'wongchukhang'),
    (u'打 鼓 嶺 ', 'takwuling'),
    (u'流 浮 山 ', 'laufaushan'),
    (u'大 埔 ', 'taipo'),
    (u'沙 田 ', 'shatin'),
    (u'屯 門 ', 'tuenmun'),
    (u'將 軍 澳 ', 'tseungkwano'),
    (u'西 貢 ', 'saikung'),
    (u'長 洲 ', 'cheungchau'),
    (u'赤 鱲 角 ', 'cheklapkok'),
    (u'青 衣 ', 'tsingyi'),
    (u'石 崗 ', 'shekkong'),
    (u'荃 灣 可 觀 ', 'tsuenwanhokoon'),
    (u'荃 灣 城 門 谷 ', 'tsuenwanshingmunvalley'),
    (u'香 港 公 園 ', 'hongkongpark'),
    (u'筲 箕 灣 ', 'shaukeiwan'),
    (u'九 龍 城 ', 'kowlooncity'),
    (u'跑 馬 地 ', 'happyvalley'),
    (u'黃 大 仙 ', 'wongtaisin'),
    (u'赤 柱 ', 'stanley'),
    (u'觀 塘 ', 'kwuntong'),
    (u'深 水 埗 ', 'shamshuipo'),
  ]

  def gettime(self, report):
    report = report.split('\n')
    for i in report:
      if re.search(u'香 港 天 文 台.*報 告', i):
        t = re.sub(u'.*香 港 天 文 台 在 ','',i)
        t = re.sub(u'發 出.*','',t)
        t = re.sub(u'上 午','AM',t)
        t = re.sub(u'下 午','PM',t)
        t = re.sub(u' ','',t)
        t = "%s "%time.localtime().tm_year + t 
        t = time.strptime(t,u'%Y %m月%d日%p%I時%M分')
        t = time.mktime(t)
        return t
    pass

  def hk0current(self, report):
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
    
