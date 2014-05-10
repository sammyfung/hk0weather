# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

#class Hk0WeatherPipeline(object):
#    def process_item(self, item, spider):
#        return item

from scrapy.exceptions import DropItem
from weatherdata.models import WeatherData

class Hk0RegionalPipeline(object):

  def process_item(self, item, spider):
    pass
    #if not WeatherData.objects.filter(reptime = item['reptime'], station=item['station']):
      #item.save()
    #else:
      #raise DropItem("Data time %s from station %s exists." % (item['reptime'],item['station'])) 
    #return item
