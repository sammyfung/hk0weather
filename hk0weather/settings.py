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
