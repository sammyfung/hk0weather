# Scrapy settings for hk0weather project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'hk0weather'

SPIDER_MODULES = ['hk0weather.spiders']
NEWSPIDER_MODULE = 'hk0weather.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hk0weather (+http://www.yourdomain.com)'

def setup_django_env(path):
  import imp, os
  from django.core.management import setup_environ
 
  f, filename, desc = imp.find_module('settings', [path])
  project = imp.load_module('settings', f, filename, desc)       
 
  setup_environ(project)
 
  # Add django project to sys.path
  import sys
  sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))
 
setup_django_env('/home/sfung/Projects/scrapy/hk0test/hk0data/hk0data')

ITEM_PIPELINES = {
  'hk0weather.pipelines.Hk0RegionalPipeline': 300,
}

