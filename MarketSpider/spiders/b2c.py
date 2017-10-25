# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from MarketSpider.items import *

import sys,json,string,requests,re




class MySpider(RedisSpider,CrawlSpider):
    name = 'market_b2c'
    redis_key="market_b2c"




    def get_info(self,select,css_lis):
        return_data=''
        for n in css_lis:
            aa=select.css(n).extract()
            if len(aa)==0:
                continue
            else:
                return_data=aa[0].strip()
        return return_data
    def re_info(self,response_body,re_str):
        try:
            data=re.findall(re_str,response_body)[0]
        except:
            data=""
        return data



    def parse(self, response):

        sel = Selector(response)
        items = []
        item = GenericItem()
        item['requirment'] ='market_b2c'
        item['url'] = response.url




        if 'jd.com' in response.url:
            item=self.spider_1(item,sel,response)
            if len(item['field1'])>0:
                items.append(item)
            return items

        if 'taobao.com' in response.url:
            item=self.spider_2(item,sel,response)
            if len(item['field1'])>0:
                items.append(item)
            return items
        if 'suning.com' in response.url:
            item=self.spider_3(item,sel,response)
            if len(item['field1'])>0:
                items.append(item)
            return items




    def spider_1(self,item,sel,response):
        # http://item.jd.com/2359567.html

        try:
            product_id=response.url.replace("http://item.jd.com/", "").replace(".html", "")
            r = requests.get('http://p.3.cn/prices/get?skuid=J_'+product_id)
            price = json.JSONDecoder().decode(r.text[1:-2])['p']
        except:
            try:
                product_id=response.url.replace("http://item.jd.com/", "").replace(".html", "")
                r = requests.get('http://p.3.cn/prices/mgets?skuIds=J_'+product_id)
                price = json.loads(r.text[1:-1])['p']
            except:
                price=""



        # 价格
        item['field2'] = price
        # 标题
        item['field1'] = self.get_info(sel,['body > div:nth-child(7) > div > div.itemInfo-wrap > div.sku-name ::text',
                                               '#name > h1 ::text',
                                               'body > div:nth-child(8) > div > div.itemInfo-wrap > div.sku-name ::text'

                                         ])

        # 分类1
        item['field3'] = self.get_info(sel,['body > div.crumb-wrap > div > div.crumb.fl.clearfix > div.item.first > a ::text',
                '#root-nav > div > div > strong > a::text',])
        # 分类2
        item['field4'] = self.get_info(sel,['body > div.crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(3) > a ::text',
                '#root-nav > div > div > span:nth-child(2) > a:nth-child(1)::text',])
        # 分类3
        item['field5'] = self.get_info(sel,['body > div.crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(5) > a ::text',
                                               '#root-nav > div > div > span:nth-child(2) > a:nth-child(2)::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['body > div.crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(7) > a ::text',
                                               'body > div.crumb-wrap > div > div.crumb.fl.clearfix > div:nth-child(7) > div > div > div.head > a ::text',
                                               '#root-nav > div > div > span:nth-child(3) > a:nth-child(1)::text'])
        # 分类5
        item['field7'] = self.get_info(sel,['body > div.crumb-wrap > div > div.crumb.fl.clearfix > div.item.ellipsis ::text',
                                               '#root-nav > div > div > span:nth-child(3) > a:nth-child(2)::text'])
        return item


    def spider_2(self,item,sel,response):
        # http://hws.m.taobao.com/cache/wdetail/5.0/?id=548240491053
        try:
            data=json.loads(response.body)
            data_one=json.loads(data['data']['apiStack'][0]['value'])

            # 标题
            item['field1']=data['data']['itemInfoModel']['title']
            # 价格
            try:
                item['field2']=data_one['data']['itemInfoModel']['priceUnits'][0]['price']
            except:
                item['field2']=""
            # 类目ID
            item['field3']=data['data']['itemInfoModel']['categoryId']
            # 卖家名称
            item['field4']=data['data']['seller']['nick']
            # 卖家id
            item['field5']=data['data']['seller']['shopId']
            # 卖家类型
            item['field6']=data['data']['seller']['type']
            # 品牌
            try:
                item['field7']=re.findall('"品牌","value":"(.*?)"',response.body)[0]
            except:
                item['field7']=""
            # 型号
            try:
                item['field8']=re.findall('"产品名称","value":"(.*?)"',response.body)[0]
            except:
                item['field8']=""

            return item

        except :
            pass


    def spider_3(self,item,sel,response):
        # http://product.suning.com/0000000000/172519947.html
        # 标题
        item['field1'] = self.re_info(response.body,'itemDisplayName":"(.*?)",')
        # 一级分类
        item['field2'] = self.re_info(response.body,'categoryName1":"(.*?)",')
        # 二级分类
        item['field3'] = self.re_info(response.body,'categoryName2":"(.*?)",')
        # 三级分类
        item['field4'] = self.re_info(response.body,'categoryName3":"(.*?)",')
        # 品牌
        item['field5'] = self.re_info(response.body,'brandName":"(.*?)",')
        # 产品名称（面包屑）
        item['field6'] = self.re_info(response.body,'seoBreadCrumbName":"(.*?)",')
        return item