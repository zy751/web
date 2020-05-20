# -*- coding: utf-8 -*-

# Scrapy settings for movieSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movieSpider'

SPIDER_MODULES = ['movieSpider.spiders']
NEWSPIDER_MODULE = 'movieSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movieSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL='WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 6

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': '__jsluid_h=6017a02f4d1d469acdd545ec1de23e3a; UM_distinctid=17143aee74c36b-0141c9cf3ab185-404b032d-100200-17143aee74d2c3; http://video.suyunbo.tv/20171015/Bnx0FNJ2/index.m3u8=5604.825057; http://hls.aoxtv.com/v2.szjal.cn/20190523/kuuoq1xL/index.m3u8=63.35983; http://hls.aoxtv.com/v2.szjal.cn/20190716/E1oyhmeN/index.m3u8=271.300218; http://youku.letv-cdn.com/2019/08/25/Drjw4n9OiG0lvhRP/playlist.m3u8=311.183022; ishistory=1; http://zy.512wx.com/20171130/YNToOeC2/index.m3u8=2.52697; CNZZDATA1273518126=1246716373-1585973826-https%253A%252F%252Fwww.sogou.com%252F%7C1587951387; PHPSESSID=icqn24bjape5eogdkfjprm3pf5; Hm_lvt_2541e9b8ba8b55898e5f914193c1209e=1587910971,1587912350,1587946821,1587953883; CNZZDATA1278661758=88093992-1585973768-https%253A%252F%252Fwww.sogou.com%252F%7C1587953157; CNZZDATA1269399177=461076216-1587903890-https%253A%252F%252Fwww.baidu.com%252F%7C1587949451; Hm_lvt_94e4bd03b9d84f1a8d2070c1010b95c1=1587910972,1587912350,1587946822,1587953884; HISTORY={video:[{"name":"","link":"http://movie.jxesk.cn[vod:link]","pic":"undefined"},{"name":"\u666E\u901A\u4EBA","link":"http://movie.jxesk.cn/play_detail/126634.html","pic":"undefined"},{"name":"\u5C0F\u72D7\u5F53\u5BB6","link":"http://movie.jxesk.cn/play_detail/34861.html","pic":"undefined"},{"name":"\u82CF\u73CA\u8BFA\u4F26\u514B\u65AF\u6D6E\u6C89\u5F55","link":"http://movie.jxesk.cn/play_detail/32896.html","pic":"undefined"},{"name":"\u5510\u5409\u8BC3\u5FB7\u5916\u4F20","link":"http://movie.jxesk.cn/play_detail/32907.html","pic":"undefined"},{"name":"\u6E05\u5E73\u4E50","link":"http://movie.jxesk.cn/play_detail/135796.html","pic":"undefined"},{"name":"\u4ECE\u4E0D\u5F88\u5C11\u6709\u65F6\u603B\u662F","link":"http://movie.jxesk.cn/play_detail/135688.html","pic":"undefined"},{"name":"\u5C0F\u732A\u4F69\u5947\u7B2C\u516D\u5B63","link":"http://movie.jxesk.cn/play_detail/93504.html","pic":"undefined"},{"name":"\u5F02\u5F624\u6D74\u706B\u91CD\u751F","link":"http://movie.jxesk.cn/play_detail/123983.html","pic":"undefined"},{"name":"\u65E0\u9650\u4E4B\u4F4F\u4EBA","link":"http://movie.jxesk.cn/play_detail/114108.html","pic":"undefined"},{"name":"\u65E0\u9650\u590D\u6D3B","link":"http://movie.jxesk.cn/play_detail/122073.html","pic":"undefined"}]}; Hm_lpvt_2541e9b8ba8b55898e5f914193c1209e=1587954320; Hm_lpvt_94e4bd03b9d84f1a8d2070c1010b95c1=1587954320'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movieSpider.middlewares.MoviespiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'movieSpider.middlewares.MoviespiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'movieSpider.pipelines.MoviespiderPipeline': 300,
    'movieSpider.pipelines.mysqlPipline':300
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
# print('1.电影 2.连续剧 3.综艺 4.动漫')
# STR=input('请输入要搜集的种类编号:\n')
STR='4'
