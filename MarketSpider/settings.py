# -*- coding: utf-8 -*-

BOT_NAME = 'MarketSpider'

SPIDER_MODULES = ['MarketSpider.spiders']
NEWSPIDER_MODULE = 'MarketSpider.spiders'



ITEM_PIPELINES = {
    'MarketSpider.pipelines.ToRedisJson': 302,
}

LOG_LEVEL = 'DEBUG'
RETRY_ENABLED = False
REDIRECT_ENABLED = False
COOKIES_ENABLED = False
CONCURRENT_REQUESTS_PER_SPIDER=300
HTTPERROR_ALLOWED_CODES = [301,302]

REACTOR_THREADPOOL_MAXSIZE=40
REDIS_HOST='61.188.255.10'
REDIS_PORT=6379
REDIS_DB=0
DOWNLOAD_TIMEOUT=10

REDIS_PARAMS={'password':'redis10'}




PROXIES = [
  {'ip_port': '133.37.31.211', 'user_pass': ''},
  {'ip_port': '133.37.31.215', 'user_pass': ''},
]


bindaddress=['127.0.0.1','127.0.0.2',
]


DOWNLOADER_MIDDLEWARES = {
    'MarketSpider.MidWare.HeaderMidWare.ProcessHeaderMidware': 500,
    'MarketSpider.MidWare.HeaderMidWare.IPProxyMiddleware': 1,
}
