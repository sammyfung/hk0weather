![hk0weather-tests.yml workflow](https://github.com/sammyfung/hk0weather/actions/workflows/hk0weather-tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/sammyfung/hk0weather/branch/master/graph/badge.svg?token=PYnOIj6SwS)](https://codecov.io/gh/sammyfung/hk0weather/)

hk0weather
===

hk0weather is an open source web scraper project using Scrapy to collect the useful weather data from Hong Kong Observatory website.

Scrapy can output collected weather data into the machine-readable formats (eg. CSV, JSON, XML).

Available Web Crawlers
---
1. **regional**: Hong Kong Regional Weather Data in 10-minutes update from HKO.    
1. **rainfall**: Hong Kong Rainfall Data in hourly update from HKO.    
1. **hkoforecast**: Hong Kong Next 24 hour Weather Forecast Report from HKO Open Data.   
1. **hko9dayforecast**: Hong Kong 9-day Weather Report from HKO Open Data.   

Installation
---

Cloning and setup hk0weather in a Py3 virtual environment   
   
   ```
   $ git clone https://github.com/sammyfung/hk0weather.git
   $ cd hk0weather
   $ python3 -m venv venv
   $ source venv/bin/activate  
   $ pip install -r requirements.txt    
   ```

Run a Scrapy spider
---

Activate the Py3 virtual environment once before the first running of web spiders.

```
$ source venv/bin/activate  
$ cd hk0weather
```

Optionally, list all available spiders.

```
$ scrapy list 
```
  
Run a regional weather data web crawler and export data to a JSON file.

```
$ scrapy crawl regional -o regional.json
```

References
--

* The background of this project: [開放源碼香港天氣計劃 hk0weather](https://sammy.hk/opensource-hk0weather/) 
* The presentation slide at BarCampHK 2013: [From Hk0weather to Open Data](http://www.slideshare.net/sammyfung/hk0weather-barcamp)

