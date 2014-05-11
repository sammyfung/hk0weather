from django.contrib import admin
from weatherdata.models import WeatherData, RainfallData

class WeatherDataAdmin(admin.ModelAdmin):
     list_display = ('scraptime', 'reptime', 'station','ename','cname','temperture','humidity','temperturemax','temperturemin','winddirection','windspeed','maxgust')
     list_filter = ['station', 'winddirection']

class RainfallDataAdmin(admin.ModelAdmin):
     list_display = ('scraptime', 'reptime', 'ename', 'cname', 'rainfall')
     list_filter = ['ename']

admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(RainfallData, RainfallDataAdmin)

