# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from weatherdata.models import WeatherData

class Hk0WeatherItem(Item):
  time = Field()
  station = Field()
  ename = Field()
  cname = Field()
  temperture = Field()
  humidity = Field()

class Hk0RegionalItemOrig(Item):
  time = Field()
  station = Field()
  ename = Field()
  cname = Field()
  temperture = Field()
  humidity = Field()
  temperturemax = Field()
  temperturemin = Field()
  winddirection = Field()
  windspeed = Field()
  maxgust = Field()

class Hk0RegionalItem(DjangoItem):
  django_model = WeatherData

class Hk0TropicalItem(Item):
  time = Field()
  postime = Field()
  x = Field()
  y = Field()
  category = Field()
  windspeed = Field()
  type = Field()
