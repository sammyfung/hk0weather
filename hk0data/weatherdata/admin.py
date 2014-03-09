from django.contrib import admin
from weatherdata.models import WeatherData

class WeatherDataAdmin(admin.ModelAdmin):
     list_display = ('time', 'station','ename','cname','temperture','humidity','temperturemax','temperturemin','winddirection','windspeed','maxgust')

admin.site.register(WeatherData, WeatherDataAdmin)

