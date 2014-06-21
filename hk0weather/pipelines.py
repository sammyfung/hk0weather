# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

#class Hk0WeatherPipeline(object):
#    def process_item(self, item, spider):
#        return item

from scrapy.exceptions import DropItem
from weatherdata.models import WeatherData, RainfallData, ReportData

class Hk0RegionalPipeline(object):

  def process_item(self, item, spider):
    if spider.name == 'regionalwx':
      if not WeatherData.objects.filter(reptime = item['reptime'], station=item['station']):
        item.save()
      else:
        raise DropItem("Weather Data time %s from station %s exists." % (item['reptime'],item['station'])) 
    elif spider.name == 'hkrainfall':
      if not RainfallData.objects.filter(reptime = item['reptime'], ename=item['ename']):
        item.save()
      else:
        raise DropItem("Rainfall Data time %s of %s exists."% (item['reptime'],item['ename']))
    elif spider.name == 'hkocurrwx' or spider.name == 'hkoforecast':
      if not ReportData.objects.filter(reptime = item['reptime'], agency = item['agency'], reptype = item['reptype'], lang = item['lang']):
        item.save()
      else:
        raise DropItem("HKO %s weather report (%s) of %s is exist."%(item['reptype'], item['lang'], item['reptime']))
    return item
