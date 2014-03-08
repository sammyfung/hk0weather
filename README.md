hk0weather
==========

hk0weather is a open source project to collect/crawl useful weather information/data from Hong Kong Observatory, and convert collected data into machine-readable format (eg. JSON).

hk0weather is written in python, with use of scrapy (a web crawl framework in python) and regular expression.

Source code is available on github.

https://github.com/sammyfung/hk0weather

Installation Example
--------------------

$ virtualenv hk0weatherenv  
$ source hk0weatherenv/bin/activate  
$ pip install scrapy  
$ git clone https://github.com/sammyfung/hk0weather.git  
$ cd hk0weather  

To crawl Current Weather Report from HKO website to json format open weather data.  
$ scrapy crawl currwx -t json -o testresult  

To crawl Regional Weather Data from HKO website to json format open weather data.  
$ scrapy crawl regionalwx -t json -o regionalwx.json


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

