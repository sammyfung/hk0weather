#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       stations.py - Hong Kong Observatory station list
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

class hko:
    stations = [
        (u'hko', 'Hong Kong Observatory'),
        (u'kp', "King's Park"),
        (u'hks', 'Wong Chuk Hang'),
        (u'tkl', 'Ta Kwu Ling'),
        (u'lfs', 'Lau Fau Shan'),
        (u'tpo', 'Tai Po'),
        (u'sha', 'Sha Tin'),
        (u'tun', 'Tuen Mun'),
        (u'jkb', 'Tseung Kwan O'),
        (u'skg', 'Sai Kung'),
        (u'cch', 'Cheung Chau'),
        (u'hka', 'Chek Lap Kok'),
        (u'ty1', 'Tsing Yi'),
        (u'sek', 'Shek Kong'),
        (u'twn', 'Tsuen Wan Ho Koon'),
        (u'tw', 'Tsuen Wan Shing Mun Valley'),
        (u'hkp', 'Hong Kong Park'),
        (u'skw', 'Shau Kei Wan'),
        (u'klt', 'Kowloon City'),
        (u'hpv', 'Happy Valley'),
        (u'wts', 'Wong Tai Sin'),
        (u'sty', 'Stanley'),
        (u'ktg', 'Kwun Tong'),
        (u'ssp', 'Sham Shui Po'),
        (u'se1', 'Kai Tak Runway Park'),
        # other regional weather stations
        (u'ksc','Kau Sai Chau'),
        (u'ngp','Ngong Ping'),
        (u'pen','Peng Chau'),
        (u'sc','Sha Chau'),
        (u'sf','Star Ferry'),
        (u'plc','Tai Mei Tuk'),
        (u'tpk','Tai Po Kau'),
        (u'tap','Tap Mun'),
        (u'tc',"Tate's Cairn"),
        (u'wgl','Waglan Island'),
        (u'wlp','Wetland Park'),
        (u'ssh','Sheung Shui'),
        (u'tyw','Pak Tam Chung'),
        (u'tms','Tai Mo Shan'),
        (u'vp1','The Peak'),
        (u'ccb','Cheung Chau Beach'),
        (u'gi','Green Island'),
        (u'se','Kai Tak'),
        (u'cp1','Central'),
        (u'swh','Sai Wan Ho'),
    ]

    cnameid = [
        (u'天文台', 'hko'),
        (u'京士柏', 'kp'),
        (u'黃竹坑', 'hks'),
        (u'打鼓嶺', 'tkl'),
        (u'流浮山', 'lfs'),
        (u'大埔', 'tpo'),
        (u'沙田', 'sha'),
        (u'屯門', 'tun'),
        (u'將軍澳', 'jkb'),
        (u'西貢', 'skg'),
        (u'長洲', 'cch'),
        (u'赤鱲角', 'hka'),
        (u'青衣', 'ty1'),
        (u'石崗', 'sek'),
        (u'荃灣可觀', 'twn'),
        (u'荃灣城門谷', 'tw'),
        (u'香港公園', 'hkp'),
        (u'筲箕灣', 'skw'),
        (u'九龍城', 'klt'),
        (u'跑馬地', 'hpv'),
        (u'黃大仙', 'wts'),
        (u'赤柱', 'sty'),
        (u'觀塘', 'ktg'),
        (u'深水埗', 'ssp'),
        (u'啟德跑道公園', 'se1'),
        # other regional weather stations
        (u'滘西洲','ksc'),
        (u'昂坪','ngp'),
        (u'坪洲','pen'),
        (u'沙洲','sc'),
        (u'天星碼頭','sf'),
        (u'大美督','plc'),
        (u'大埔滘','tpk'),
        (u'塔門','tap'),
        (u'大老山','tc'),
        (u'橫瀾島','wgl'),
        (u'濕地公園','wlp'),
        (u'上水','ssh'),
        (u'北潭涌','tyw'),
        (u'大帽山','tms'),
        (u'山頂','vp1'),
        (u'長洲泳灘','ccb'),
        (u'青洲','gi'),
        (u'啟德','se'),
        (u'中環','cp1'),
        (u'西灣河','swh'),
    ]

    def getename(self, id):
        for i in self.stations:
            if id in i:
                return i[1]

    def getcname(self, id):
        for i in self.cnameid:
            if id in i:
                return i[0]
