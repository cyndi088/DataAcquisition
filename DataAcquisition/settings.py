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
# MONGO_USER = 'admin'
# MONGO_PSW = 'admin'
MONGO_DB = 'eleme'

MYSQL_HOST = "192.168.10.121"
MYSQL_USER = 'hzyg'
MYSQL_PASSWORD = '@hzyq20180426..'
MYSQL_DB = 'yfhunt'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DataAcquisition (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

DOWNLOAD_TIMEOUT = 10
HTTPPROXY_ENABLED = True
PROXIES = [
    "http://183.135.253.38:36974",
    "http://223.242.246.26:35714",
    "http://119.180.131.123:8060",
    "http://183.135.250.188:33704",
    "http://60.175.199.186:37541",
    "http://183.129.244.13:10080",
    "http://120.39.160.216:45703",
    "http://123.161.156.155:32989",
    "http://118.190.95.35:9001",
    "http://123.55.92.61:26413"]

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

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/68.0.3440.106 Safari/537.36',
  'Referer': 'https://www.ele.me/place/wtm5uruvh6rm?latitude=30.233873&longitude=119.724733',
  'Cookie': 'ubt_ssid=0wc8wcpdkke5njouu3l1o2votf4zies0_2018-09-06; _utrace=f3364b7f625039862ebaf21cd2037c8f_2018-09-06;'
            ' track_id=1536212355|a092177d5800c1678ae6b3d425c46b1d1e830a3adfdf3071b7|09180fb9aa0f4903a3bbefd1c8e3ffe0; '
            'USERID=1817989241; SID=vRI4q3x4CZU68lGCQlP6TbeNOghPRj5P5UCQ'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'DataAcquisition.middlewares.DataacquisitionSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'DataAcquisition.middlewares.DataacquisitionDownloaderMiddleware': 543,
   'DataAcquisition.middlewares.RandomProxyMiddleware': 543
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

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
