try:
    from scrapy_djangoitem import DjangoItem
    from openweather.models import WeatherData, RainfallData, ReportData

    class Hk0RegionalItem(DjangoItem):
        django_model = WeatherData

    class Hk0RainfallItem(DjangoItem):
        django_model = RainfallData

    class ReportItem(DjangoItem):
        django_model = ReportData
except ImportError:
    from scrapy.item import Item, Field

    class Hk0RegionalItem(Item):
        scraptime = Field()
        reptime = Field()
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
        pressure = Field()

    class Hk0RainfallItem(Item):
        scraptime = Field()
        reptime = Field()
        ename = Field()
        cname = Field()
        rainfall = Field()

    class ReportItem(Item):
        reptime = Field()
        agency = Field()
        reptype = Field()
        lang = Field()
        report = Field()

    class Hk0WeatherItem(Item):
        time = Field()
        station = Field()
        ename = Field()
        cname = Field()
        temperture = Field()
        humidity = Field()

    class Hk0TropicalItem(Item):
        time = Field()
        postime = Field()
        x = Field()
        y = Field()
        category = Field()
        windspeed = Field()
        tctype = Field()


