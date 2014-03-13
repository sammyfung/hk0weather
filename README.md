hk0weather
==========

hk0weather is a open source project to scrap useful weather data from Hong Kong Observatory, it is written in python.

With scrapy web scraping framework and regular expression library, collected weather data can be converted to machine-readable formats (eg. JSON).

With django web framework, collected weather data will be stored in django, and accessible through django web admin UI. sqlite3 is default database file format, and it can be connected with MySQL and other database systems supported by django.

Source code is available on github.

https://github.com/sammyfung/hk0weather

Installation Example
--------------------

$ virtualenv hk0weatherenv  
$ source hk0weatherenv/bin/activate  
$ pip install scrapy  
$ pip install django    
$ git clone https://github.com/sammyfung/hk0weather.git  
$ cd hk0data   
$ python manage.py syncdb    
$ python manage.py runserver &    
$ cd ..   
$ cd hk0weather  

To scrap Current Weather Report from HKO website to json format open weather data. (data won't be stored to django)   
$ scrapy crawl currwx -t json -o testresult  

To scrap Regional Weather Data from HKO website to json format open weather data, and stored in django.  
$ scrapy crawl regionalwx -t json -o regionalwx.json

Django web admin UI can be access at:   
http://localhost:8000/admin

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

