from scrapy.item import Item, Field
from scrapy_djangoitem import DjangoItem
from openweather.models import WeatherData, RainfallData, ReportData

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

class ReportItem(DjangoItem):
    django_model = ReportData
