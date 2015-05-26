from django.http import HttpResponse, Http404
from weatherdata.models import WeatherData
from datetime import datetime, timedelta
import json, pytz

def regional_weather_data(request):
  # 1. Latest measurement at all stations or individual stations in past 24 hours.
  # 2. 24 hour data if start_time is supplied by user.
  station_id = request.GET.get('id', 0)
  start_time = request.GET.get('start', 0)
  if start_time != 0:
    oldest_time = datetime.strptime(start_time, "%Y%m%d")
  if station_id != 0:
    if start_time == 0:
      oldest_time = datetime.now() - timedelta(days=1)
    data = WeatherData.objects.values().filter(station = station_id, reptime__gte = oldest_time)[0:24]
  else: 
    if start_time == 0:
      oldest_time = datetime.now() - timedelta(hours=2)
    data = WeatherData.objects.values().filter(reptime__gte = oldest_time)

  # return in JSON data format or 404 if no data.
  if len(data) == 0:
    raise Http404
  json_data = []
  #latest_time = WeatherData.objects.order_by('-reptime')[0].reptime.isoformat()
  #for station in WeatherData.objects.values().filter(reptime = latest_time):
  for station in data:
    hkt = pytz.timezone('Asia/Hong_Kong')
    station['reptime'] = station['reptime'].astimezone(hkt).isoformat()
    station['scraptime'] = station['scraptime'].astimezone(hkt).isoformat()
    json_data = json_data + [ station ]
  return HttpResponse(json.dumps(json_data), content_type="application/json")

