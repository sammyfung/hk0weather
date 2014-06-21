from django.contrib import admin
from weatherdata.models import WeatherData, RainfallData, ReportData

class WeatherDataAdmin(admin.ModelAdmin):
     list_display = ('scraptime', 'reptime', 'station','ename','cname','temperture','humidity','temperturemax','temperturemin','winddirection','windspeed','maxgust')
     list_filter = ['station', 'winddirection']

class RainfallDataAdmin(admin.ModelAdmin):
     list_display = ('scraptime', 'reptime', 'ename', 'cname', 'rainfall')
     list_filter = ['ename']

class ReportDataAdmin(admin.ModelAdmin):
     list_display = ('reptime', 'agency', 'reptype', 'lang', 'report')
     list_filter = ['agency', 'reptype', 'lang']

admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(RainfallData, RainfallDataAdmin)
admin.site.register(ReportData, ReportDataAdmin)
