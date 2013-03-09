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
$ scrapy crawl currwx -t json -o testresult  

Reference
---------

I introduced this project on my following Chinese blog.

http://sammy.hk/2013/02/14/opensource-hk0weather

And I also presented it at BarCampHK 2013 and a local open source workshop, hereby is my slide.

http://www.slideshare.net/sammyfung/hk0weather-barcamp

