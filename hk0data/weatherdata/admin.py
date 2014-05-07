from django.contrib import admin
from weatherdata.models import WeatherData

class WeatherDataAdmin(admin.ModelAdmin):
     list_display = ('scraptime', 'reptime', 'station','ename','cname','temperture','humidity','temperturemax','temperturemin','winddirection','windspeed','maxgust')
     list_filter = ['station', 'winddirection']

admin.site.register(WeatherData, WeatherDataAdmin)

