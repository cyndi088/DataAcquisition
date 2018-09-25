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

"""MONGODB 配置链接"""
# MONGO_HOST = '106.14.176.62'
MONGO_HOST = '192.168.10.125'
MONGO_PORT = 27017
# MONGO_USER = 'admin'
# MONGO_PSW = 'admin'
MONGO_DB = 'eleme'

"""MYSQL 配置链接"""
MYSQL_HOST = "192.168.10.121"
MYSQL_USER = 'hzyg'
MYSQL_PASSWORD = '@hzyq20180426..'
MYSQL_DB = 'yfhunt'

"""REDIS 配置链接"""
REDIS_URL = "redis://127.0.0.1:6379"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DataAcquisition (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 12

RETRY_TIMES = 1

DOWNLOAD_TIMEOUT = 5
HTTPPROXY_ENABLED = True


# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

HTTPERROR_ALLOWED_CODES = [401]


# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'application/json, text/plain, */*',
  # 'Accept-Language': 'zh-CN,zh;q=0.9',
  # 'Path': '/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wtm5uruvh6rm&latitude=30.233873&limit=24'
  #         '&longitude=119.724733&offset=72&terminal=web',
  # 'Scheme': 'https',
  # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
  #               'Chrome/68.0.3440.106 Safari/537.36',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN',
  # 'Referer': 'https://www.ele.me/place/wtm5uruvh6rm?latitude=30.233873&longitude=119.724733',
  # 'Cookie': 'ubt_ssid=0wc8wcpdkke5njouu3l1o2votf4zies0_2018-09-06; _utrace=f3364b7f625039862ebaf21cd2037c8f_2018-09-06;'
  #           ' eleme__ele_me=dcacbd1c8e391dea0149f8ac77bb1b10%3A91a2c47adf54f9ebf3572011b0fe6931e88d0ca2;'
  #           ' track_id=1536212355|a092177d5800c1678ae6b3d425c46b1d1e830a3adfdf3071b7|09180fb9aa0f4903a3bbefd1c8e3ffe0;'
  #           ' USERID=276010313; SID=6siLPTqa3hWTsK4ErtOW5oHwSEJdiTYPvW9Q',
  'Cookie': 'SID=lVstC4FAOsyjj3WEl4ct9Bfq2BqIL7WtWk5w; _utrace=b394325f0b5c8ed39f175f6d7ca42737_2018-09-20; ubt_ssid=conxzxx08xy0il6fe0eqmnjosa71awt5_2018-09-20; perf_ssid=ioqf4z05g40l9rqiz32je8sd7wzr59f3_2018-09-20'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'DataAcquisition.middlewares.DataacquisitionSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'DataAcquisition.middlewares.DataacquisitionDownloaderMiddleware': 543,
   'DataAcquisition.middlewares.RandomProxyMiddleware': 543,
   # 'DataAcquisition.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   # 'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'DataAcquisition.pipelines.DataacquisitionPipeline': 300,
   'DataAcquisition.pipelines.MongodbPipeline': 350,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
