# -*- coding: utf-8 -*-

# Scrapy settings for DataAcquisition project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DataAcquisition'

SPIDER_MODULES = ['DataAcquisition.spiders']
NEWSPIDER_MODULE = 'DataAcquisition.spiders'

# MONGO_HOST = '106.14.176.62'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USER = 'llps'
# MONGO_PSW = 'llps&789'
MONGO_DB = 'eleme'
MONGO_COLL = 'cities'

MYSQL_HOST = "192.168.10.121"
MYSQL_USER = 'hzyg'
MYSQL_PASSWORD = '@hzyq20180426..'
MYSQL_DB = 'yfhunt'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DataAcquisition (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'application/json, text/plain, */*',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#   'Cookie': 'ubt_ssid=33o082pi39m1xaftltj45loe51cn0dqz_2018-07-18; _utrace=9c3e0f93446bfff24e0614e219fd9b17_2018-07-18; eleme__ele_me=bbc480410bb940b35df8af170634bfe6%3Ae6eb2d41dc069edbeb37b3c66dc6f5bcd6e9da4b; track_id=1534214884|1c434f626ff2031c0a5f16c09a5ec5f59e531e81f8f3e5d715|766ada6cac516085709b1a21a5203ba4; USERID=276010313; SID=mJmhEeoydh3sqnakcYO2QtzhVvUA7QfeXE1A'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DataAcquisition.middlewares.DataacquisitionSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DataAcquisition.middlewares.DataacquisitionDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'DataAcquisition.pipelines.DataacquisitionPipeline': 300,
    'DataAcquisition.pipelines.MongodbPipeline': 350,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
