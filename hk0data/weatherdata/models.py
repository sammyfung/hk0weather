from django.db import models

class WeatherData(models.Model):
  scraptime = models.DateTimeField()
  reptime = models.DateTimeField()
  station = models.CharField(max_length=3)
  ename = models.CharField(max_length=64)
  cname = models.CharField(max_length=16)
  temperture = models.FloatField(null=True, blank=True)
  humidity = models.IntegerField(null=True, blank=True)
  temperturemax = models.FloatField(null=True, blank=True)
  temperturemin = models.FloatField(null=True, blank=True)
  winddirection = models.CharField(max_length=16,null=True, blank=True)
  windspeed = models.IntegerField(null=True, blank=True)
  maxgust = models.IntegerField(null=True, blank=True)

class RainfallData(models.Model):
  scraptime = models.DateTimeField()
  reptime = models.DateTimeField()
  ename = models.CharField(max_length=64)
  cname = models.CharField(max_length=16, null=True, blank=True)
  rainfall = models.IntegerField(null=True, blank=True)
