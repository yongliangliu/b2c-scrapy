# -*- coding: utf-8 -*-
import json
from scrapy.conf import settings
import redis






class ToRedisJson(object):
    def __init__(self):
        self.server = '61.188.255.10'
        self.port = '6379'
        self.db = '0'
        self.key_name = "market_result"
        self.password ='redis10'

        self.r=redis.Redis(host=self.server,port=self.port,db=self.db,password=self.password)

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        a=self.r.lpush(self.key_name,line)
        return item


