from django.conf.urls import patterns, url

from weatherdata import views

urlpatterns = patterns('',
    url(r'^api/regional/$', views.regional_weather_data),
    url(r'^$', views.regional_weather_data),
)
