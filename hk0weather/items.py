# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Hk0WeatherItem(Item):
  time = Field()
  station = Field()
  temperture = Field()
  humidity = Field()

class Hk0RegionalItem(Item):
  time = Field()
  station = Field()
  temperture = Field()
  humidity = Field()
  temperturemax = Field()
  temperturemin = Field()

