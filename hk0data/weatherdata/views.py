from django.http import HttpResponse
from weatherdata.models import WeatherData
from datetime import datetime, timedelta
import json, pytz

def regional_weather_data(request):
  station = request.GET.get('id', '')
  json_data = {}
  latest_time = WeatherData.objects.order_by('-reptime')[0].reptime.__str__()
  for station in WeatherData.objects.values().filter(reptime = latest_time):
    json_data[station['station']] = station
    hkt = pytz.timezone('Asia/Hong_Kong')
    json_data[station['station']]['reptime'] = station['reptime'].astimezone(hkt).__str__()
    json_data[station['station']]['scraptime'] = station['scraptime'].astimezone(hkt).__str__()
  return HttpResponse(json.dumps(json_data), content_type="application/json")

