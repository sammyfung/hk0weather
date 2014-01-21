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
    (u'天文台', 'hko'),
    (u'京士柏', 'kingspark'),
    (u'黃竹坑', 'wongchukhang'),
    (u'打鼓嶺', 'takwuling'),
    (u'流浮山', 'laufaushan'),
    (u'大埔', 'taipo'),
    (u'沙田', 'shatin'),
    (u'屯門', 'tuenmun'),
    (u'將軍澳', 'tseungkwano'),
    (u'西貢', 'saikung'),
    (u'長洲', 'cheungchau'),
    (u'赤鱲角', 'cheklapkok'),
    (u'青衣', 'tsingyi'),
    (u'石崗', 'shekkong'),
    (u'荃灣可觀', 'tsuenwanhokoon'),
    (u'荃灣城門谷', 'tsuenwanshingmunvalley'),
    (u'香港公園', 'hongkongpark'),
    (u'筲箕灣', 'shaukeiwan'),
    (u'九龍城', 'kowlooncity'),
    (u'跑馬地', 'happyvalley'),
    (u'黃大仙', 'wongtaisin'),
    (u'赤柱', 'stanley'),
    (u'觀塘', 'kwuntong'),
    (u'深水埗', 'shamshuipo'),
    # other regional weather stations
    (u'滘西洲','kausaichau'),
    (u'昂坪','ngongping'),
    (u'坪洲','pengchau'),
    (u'沙洲','shachau'),
    (u'天星碼頭','starferry'),
    (u'大美督','taimeituk'),
    (u'大埔滘','taipokau'),
    (u'塔門','tapmun'),
    (u'大老山','tatescairn'),
    (u'橫瀾島','waglanisland'),
    (u'濕地公園','wetlandpark'),
    (u'上水','sheungshui'),
    (u'北潭涌','paktamchung'),
    (u'大帽山','taimoshan'),
    (u'山頂','thepeak'),
    (u'長洲泳灘','cheungchaubeach'),
    (u'青洲','greenisland'),
    (u'啟德','kaitak'),
    (u'中環','central'),
    (u'西灣河','saiwanho'),
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
  
  def gettime2(self, report):
    report = report.split('\n')
    for i in report:
      if re.search(u'錄得的天氣資料', i):
        t = re.sub(u'錄得的天氣資料.*','', i)
        t = re.sub(u' ','', t)
        t = time.strptime(t,u'%Y年%m月%d日%I時%M分')
        t = time.mktime(t)
        return t

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
    
