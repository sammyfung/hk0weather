hk0weather
==========

hk0weather is a open source project to scrape useful weather data from Hong Kong Observatory website, it is written in python.

With scrapy web scraping framework and regular expression library, collected weather data can be converted to machine-readable formats (eg. JSON).

This scrapy project can be run with / without Django.    

With django web framework, collected weather data will be stored in django, and accessible through django web admin UI. sqlite3 is default database file format, and it can be connected with MySQL and other database systems supported by django.

Source code is available on github.

https://github.com/sammyfung/hk0weather

Installation Example
--------------------

1) Setting up python 3 virtual enviornment and cloning hk0weather   
   
$ virtualenv hk0weatherenv  
$ source hk0weatherenv/bin/activate  
$ pip install Scrapy Django scrapy-djangoitem pytz    
$ git clone https://github.com/sammyfung/hk0weather.git    
    
2) Setting openweather   

$ django-admin startproject yourprojname   
$ cd yourprojname   
$ git clone https://github.com/sammyfung/openweather.git   
   
Please also add openweather app to your django setting, and then do the following to alter django database tables.

$ ./manage.py makemigrations    
$ ./manage.py migrate   

3) Setting enviornment variables for hk0weather   
   
$ cd your-path-to/hk0weather     
$ export PYTHONPATH=/your-path-to/yourprojname    
$ export DJANGO_SETTINGS_MODULE=yourprojname.settings

Running a Django CMS (with web admin UI)
----------------------------------------

$ cd /your-path-to/yourprojname    
$ python manage.py runserver &  


Django web admin UI can be access at: http://localhost:8000/admin  

Run a scrapy web scraper
------------------------

Setting 2 enviornment variables linking with your django project with openweather app installed.    
$ export PYTHONPATH=/your-path-to/yourdjangoprojname     
$ export DJANGO_SETTINGS_MODULE=yourdjangoprojname.settings

To run a scrapy web scraper.   
$ scrapy crawl <name of scraper>   

To run a scrapy web scraper with output file in json format.   
$ scrapy crawl <name of scraoer> -o output_filename -t json    

List of Spiders
---------------
1. hko9dayforecast (under development): Hong Kong 9 day Weather Report from HKO.   
2. hkocurrwx: Current Hourly Hong Kong Weather Report from HKO.    
3. hkoforecast: Hong Kong Next 24 hour Weather Forecast Report from HKO.   
4. hkrainfall: Hong Kong Rainfall Data (Hourly update) from HKO.    
5. regionalwx: Hong Kong Regional Weather Data (10-min update) from HKO.    

Mailing List
------------

For general discussion of hk0weather project, please go to hk0weather google group. Please feel freely to ask questions or post your suggestions / comments.

https://groups.google.com/forum/#!forum/hk0weather


Reference
---------

I introduced this project on my following Chinese blog.

http://sammy.hk/2013/02/14/opensource-hk0weather

And I also presented it at BarCampHK 2013 and a local open source workshop, hereby is my slide.

http://www.slideshare.net/sammyfung/hk0weather-barcamp

