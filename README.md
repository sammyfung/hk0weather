[![Build Status](https://travis-ci.com/sammyfung/hk0weather.svg?branch=master)](https://travis-ci.com/sammyfung/hk0weather)

hk0weather
===

hk0weather is an open source web scraper project using Scrapy to collect the useful weather data from Hong Kong Observatory website.

Scrapy can output collected weather data into the machine-readable formats (eg. CSV, JSON, XML).

Optionally, this project supports a Django app 'openweather' to store the collected weather data to Django web framework, and the data can be shown on web through the Django admin UI.

Available Spiders
---
1. **regional**: Hong Kong Regional Weather Data in 10-minutes update from HKO.    
1. **rainfall**: Hong Kong Rainfall Data in hourly update from HKO.    
1. **hkoforecast**: Hong Kong Next 24 hour Weather Forecast Report from HKO Open Data.   
1. **hko9dayforecast**: Hong Kong 9-day Weather Report from HKO Open Data.   

Installation Example
---

1) Cloning and setup hk0weather in a Py3 virtual environment   
   
   ```
   git clone https://github.com/sammyfung/hk0weather.git  
   virtualenv hk0weatherenv  
   source hk0weatherenv/bin/activate  
   cd hk0weather   
   pip install -r requirements.txt    
   ```
    
2) Optional: Setup hk0weather to use openweather

   ```
   pip install -r requirements-with-django.txt    
   cd ..   
   django-admin startproject yourweatherproject   
   cd yourweatherproject   
   git clone https://github.com/sammyfung/openweather.git   
   ```
   
   Please add 'openweather' to INSTALLED_APPS in Django yourweatherproject/settings.py.
   
   ```
   ./manage.py makemigrations    
   ./manage.py migrate   
   ./manage.py createsuperuser   
   ./manage.py runserver &    
   cd ../hk0weather     
   ```
   
   Django daemon is now running in the background, its web admin UI can be access at [http://localhost:8000/admin](http://localhost:8000/admin). 
   
   ```
   export PYTHONPATH=/your-full-path-to/yourweatherproject    
   export DJANGO_SETTINGS_MODULE=yourweatherproject.settings   
   ```
   
   Please export PYTHONPATH and DJANGO_SETTINGS_MODULE again after every activation of the Py3 virtual environment.

Run a Scrapy spider
---

Activate the Py3 virtual environment once before the first running of web spiders.

```
source hk0weatherenv/bin/activate  
```

Optionally, if Django is in use, export PYTHONPATH and DJANGO_SETTINGS_MODULE.

```
export PYTHONPATH=/your-full-path-to/yourweatherproject    
export DJANGO_SETTINGS_MODULE=yourweatherproject.settings   
```
Optionally, list all available spiders.

```
scrapy list 
```
  
Run a specific spider (eg. regional) in Scrapy

```
scrapy crawl regional   
```

and optionally use -t (file format) and -o (filename) to output the data in a json file.
   
```
scrapy crawl regional -t json -o test.json
```

References
--

* The background of this project: [開放源碼香港天氣計劃 hk0weather](https://sammy.hk/opensource-hk0weather/) 
* The presentation slide at BarCampHK 2013: [From Hk0weather to Open Data](http://www.slideshare.net/sammyfung/hk0weather-barcamp)

