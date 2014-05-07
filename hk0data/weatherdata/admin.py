from django.contrib import admin
from weatherdata.models import WeatherData

class WeatherDataAdmin(admin.ModelAdmin):
     list_display = ('scraptime', 'reptime', 'station','ename','cname','temperture','humidity','temperturemax','temperturemin','winddirection','windspeed','maxgust')

admin.site.register(WeatherData, WeatherDataAdmin)

