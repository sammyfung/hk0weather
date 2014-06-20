# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from weatherdata.models import WeatherData, RainfallData

class Hk0WeatherItem(Item):
  time = Field()
  station = Field()
  ename = Field()
  cname = Field()
  temperture = Field()
  humidity = Field()

class Hk0RegionalItem(DjangoItem):
  django_model = WeatherData

class Hk0TropicalItem(Item):
  time = Field()
  postime = Field()
  x = Field()
  y = Field()
  category = Field()
  windspeed = Field()
  tctype = Field()

class Hk0RainfallItem(DjangoItem):
  django_model = RainfallData

class HkocurrwxItem(Item):
  reptime = Field()
  lang = Field()
  report = Field()
