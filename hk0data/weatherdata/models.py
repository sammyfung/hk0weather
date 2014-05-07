from django.db import models

class WeatherData(models.Model):
  scraptime = models.FloatField()
  reptime = models.IntegerField()
  station = models.CharField(max_length=3)
  ename = models.CharField(max_length=64)
  cname = models.CharField(max_length=16)
  temperture = models.FloatField(null=True)
  humidity = models.IntegerField(null=True)
  temperturemax = models.FloatField(null=True)
  temperturemin = models.FloatField(null=True)
  winddirection = models.CharField(max_length=16,null=True)
  windspeed = models.IntegerField(null=True)
  maxgust = models.IntegerField(null=True)

