# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider

from MarketSpider.items import *

import sys,string,requests,json
from scrapy import log

class MySpider(RedisSpider,CrawlSpider):
    name = 'market_travel'
    redis_key="market_travel"


    def get_info(self,select,css_lis):
        return_data=''
        for n in css_lis:
            aa=select.css(n).extract()
            if len(aa)==0:
                continue
            else:
                return_data=aa[0].strip()
        return return_data


    def parse(self, response):
        sel = Selector(response)
        items = []
        item = GenericItem()

        item['requirment'] ='market_travel'
        item['url'] = response.url

        if 'www.tuniu.com/tour' in response.url:
            item=self.spider_1(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'www.tuniu.com/tours' in response.url:
            item=self.spider_2(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.tuniu.com/journey/' in response.url:
            item=self.spider_3(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.tuniu.com/visa/visa' in response.url:
            item=self.spider_4(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items



        elif 'www.tuniu.com/tucom/' in response.url:
            item=self.spider_5(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'www.tuniu.com/cruise' in response.url:
            item=self.spider_6(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'www.tuniu.com/flight/intel/portal/charterFlightDetail?productId=' in response.url:
            item=self.spider_7(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'globalhotel.tuniu.com/gdetail' in response.url:
            item=self.spider_8(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'hotel.tuniu.com/detail' in response.url:
            item=self.spider_9(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'menpiao.tuniu.com/t' in response.url:
            item=self.spider_10(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'temai.tuniu.com/tours' in response.url:
            item=self.spider_11(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.tuniu.com/way' in response.url:
            item=self.spider_12(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'www.tuniu.com/trips' in response.url:
            item=self.spider_13(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'bbs.qyer.com/thread' in response.url:
            item=self.spider_14(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'place.qyer.com/poi' in response.url:
            item=self.spider_15(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'z.qyer.com/deal' in response.url:
            item=self.spider_16(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'package.qunar.com/user/detail' in response.url:
            item=self.spider_17(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'items.fliggy.com/item.htm' in response.url:
            item=self.spider_18(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'hotels.ctrip.com/international' in response.url:
            item=self.spider_19(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'hotels.ctrip.com/apartment' in response.url:
            item=self.spider_20(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'taocan.ctrip.com/freetravel' in response.url:
            item=self.spider_21(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'vacations.ctrip.com/grouptravel' in response.url:
            item=self.spider_22(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'cruise.ctrip.com/c' in response.url:
            item=self.spider_23(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'vacations.ctrip.com/dingzhi' in response.url:
            item=self.spider_24(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'vacations.ctrip.com/youxue' in response.url:
            item=self.spider_25(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'vacations.ctrip.com/visa' in response.url:
            item=self.spider_26(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.hhtravel.com/product' in response.url:
            item=self.spider_27(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'vacations.ctrip.com/insurance' in response.url:
            item=self.spider_28(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'flights.ctrip.com/international' in response.url:
            item=self.spider_29(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'rails.ctrip.com/passdetails' in response.url:
            item=self.spider_30(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items


        elif 'piao.ctrip.com/dest' in response.url:
            item=self.spider_31(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'huodong.ctrip.com/activity' in response.url:
            item=self.spider_32(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'you.ctrip.com/sight' in response.url:
            item=self.spider_33(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'g.ctrip.com/merchant/detail' in response.url:
            item=self.spider_34(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.mafengwo.cn/travel-scenic-spot/mafengwo' in response.url:
            item=self.spider_35(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.mafengwo.cn/gonglve' in response.url:
            item=self.spider_36(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.mafengwo.cn/sales' in response.url:
            item=self.spider_37(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'www.mafengwo.cn/hotel' in response.url:
            item=self.spider_38(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items

        elif 'zh.airbnb.com/rooms' in response.url:
            item=self.spider_39(item,sel)
            if len(item['field1'])>0:
                items.append(item)
            return items




    def spider_1(self,item,sel):
        # http://www.tuniu.com/tour/210138673
        # 价格
        item['field2'] = self.get_info(sel,['#J_ResourcePrice > div > div.resource-section-content > span.price-quantity > span.price-number ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['body > div.product-body.product-tour > div > div.resource > h1 > strong ::text'])
        return item

    def spider_2(self,item,sel):
        # http://www.tuniu.com/tours/210328902
        # 价格
        item['field2'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.product_info > div.product_main_bar > div.product_right > div.product_price_bar.new_price_bar.clearfix > div.new_price > p > span.price ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.product_info > div.product_name_bar > h1 ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.search_nav > p > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.search_nav > p > a:nth-child(2) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.search_nav > p > a:nth-child(3) ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.search_nav > p > a:nth-child(4) ::text'])
        # 分类5
        item['field7'] = self.get_info(sel,['#index1200 > div.wrapper_bg > div > div.search_nav > p > a:nth-child(5) ::text'])
        return item

    def spider_3(self,item,sel):
        #http://www.tuniu.com/journey/500
        # 价格
        item['field2'] = self.get_info(sel,['body > div.play-body > div > div.brief > div.brief-info > div.brief-overview > div.brief-price-preview > span > strong ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['body > div.play-body > div > div.brief > div.brief-info > div.brief-title > h1 ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['body > div.play-body > div > div.crumbs > p > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['body > div.play-body > div > div.crumbs > p > a:nth-child(2) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['body > div.play-body > div > div.crumbs > p > a:nth-child(3) ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['body > div.play-body > div > div.crumbs > p > a:nth-child(4) ::text'])
        # 分类5
        item['field7'] = self.get_info(sel,['body > div.play-body > div > div.crumbs > p > a:nth-child(5) ::text'])
        return item


    def spider_4(self,item,sel):
        #http://www.tuniu.com/visa/visa_210423750/
        # 价格
        item['field2'] = self.get_info(sel,['#index1200 > div.g-main.visa-prodct-detail > div > div.m-product-summary.clearfix > div.box-right > div.product-info2 > div:nth-child(1) > em ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['#index1200 > div.g-main.visa-prodct-detail > div > div.m-product-summary.clearfix > div.box-right > h2 ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#index1200 > div.g-main.visa-prodct-detail > div > ul > li:nth-child(1) > a ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#index1200 > div.g-main.visa-prodct-detail > div > ul > li:nth-child(3) > a ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#index1200 > div.g-main.visa-prodct-detail > div > ul > li.cur ::text'])
        return item



    def spider_5(self,item,sel):
        #http://www.tuniu.com/tucom/210214192
        # 价格
        item['field2'] = self.get_info(sel,[])
        # 标题
        item['field1'] = self.get_info(sel,['#wrapMain > div.mainContent > div.main_top > div > form > div > div.product_name ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#wrapMain > div.search_nav > p > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#wrapMain > div.search_nav > p > a:nth-child(2) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#wrapMain > div.search_nav > p > a:nth-child(3) ::text'])
        return item


    def spider_6(self,item,sel):
        #http://www.tuniu.com/cruise/6281359
        # 价格
        item['field2'] = self.get_info(sel,['#zizhu_main > div.zizhu_right > div > div > dl:nth-child(2) > dd > span.zizhuPrice > em ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['#toursPowerFloatAsync > div > div.tours_title > h1 ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['body > div.wrap.clearfix > div > div.search_nav > p > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['body > div.wrap.clearfix > div > div.search_nav > p > a:nth-child(2) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['body > div.wrap.clearfix > div > div.search_nav > p > a:nth-child(3) ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['body > div.wrap.clearfix > div > div.search_nav > p > a:nth-child(4) ::text'])
        return item

    def spider_7(self,item,sel):
        #http://www.tuniu.com/flight/intel/portal/charterFlightDetail?productId=313
        # 标题
        item['field1'] = self.get_info(sel,['#charterFlightDetail > h3 ::text'])
        return item


    def spider_8(self,item,sel):
        #http://globalhotel.tuniu.com/gdetail/1503111068/?checkInDate=2017-05-02&checkOutDate=2017-05-03
        # 价格
        item['field2'] = self.get_info(sel,['#hotelPriceAndTax > span.rmbStartPrice_large  ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['#wrap > div.detail_title.clearfix > div.title_hotelName.fl.clearfix > div.title_hotelName01.clearfix > div > span.name_font ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#wrap > div.path_bar.clearfix > p > a:nth-child(2) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#wrap > div.path_bar.clearfix > p > a:nth-child(3) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#wrap > div.path_bar.clearfix > p > a:nth-child(4) ::text'])
        return item

    def spider_9(self,item,sel):
        #http://hotel.tuniu.com/detail/198008350
        # 价格
        item['field2'] = self.get_info(sel,['#startPrice ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['#hotelName ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#container > div.search_nav > p > a:nth-child(2) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#container > div.search_nav > p > a:nth-child(3) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#container > div.search_nav > h1 ::text'])
        return item

    def spider_10(self,item,sel):
        #http://menpiao.tuniu.com/t_9964
        # 价格
        item['field2'] = self.get_info(sel,['body > div.v2_body > div > div.v2_w1189 > div.v2_ticket_proinf.clearfix > div.v2_tp_text > div.v2-price > span.v2-money ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['body > div.v2_body > div > div.v2_w1189 > div.v2_ticket_proinf.clearfix > div.v2_tp_text > div.v2_ct_title ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['body > div.v2_body > div > div.v2_search_nav > p > a:nth-child(2) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['body > div.v2_body > div > div.v2_search_nav > p > a:nth-child(3) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['body > div.v2_body > div > div.v2_search_nav > p > a:nth-child(4) ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['body > div.v2_body > div > div.v2_search_nav > p > span:nth-child(6) ::text'])

        return item

    def spider_11(self,item,sel):
        #http://temai.tuniu.com/tours/212092757
        # 价格
        item['field2'] = self.get_info(sel,['#block_detail > div.panel.product_info.product_outline > div.panel-body > div.product_main_bar > div.product_right > div.product_price_bar.product_price_bar_height > div.price_bar > dl > dd > span.sale_price.price_tips ::text'])
        # 标题
        item['field1'] = self.get_info(sel,['#block_detail > div.panel.product_info.product-info-name > div.panel-body > div.product_name_bar > h1 ::text'])

        return item

    def spider_12(self,item,sel):
        #http://www.tuniu.com/way/3590314
        # 分类1
        item['field3'] = u'攻略'
        # 分类2
        item['field4'] = u'玩法'
        # 标题
        item['field1'] = self.get_info(sel,['body > div.detai-content > div.detail-top > div.detail-show > div > div > div ::text'])
        return item


    def spider_13(self,item,sel):
        #http://www.tuniu.com/trips/12540960
        # 分类1
        item['field3'] = u'攻略'
        # 分类2
        item['field4'] = u'游记'
        # 标题
        item['field1'] = self.get_info(sel,['body > div.detail-main > div.detail-show.detail-show-notit > div.detail-title-bg > div > h1 ::text'])
        return item


    def spider_14(self,item,sel):
        #http://bbs.qyer.com/thread-2704880-1.html
        # 分类1
        item['field3'] = u'穷游'
        # 分类2
        item['field4'] = u'论坛'
        # 分类3
        item['field1'] = self.get_info(sel,['head > title ::text'])
        return item



    def spider_15(self,item,sel):
        #http://place.qyer.com/poi/V2wJa1FmBzBTbQ/
        # 标题
        item['field1'] = self.get_info(sel,['body > div.poi-bg.clearfix > div.poi-top > div > div.poi-largeTit > h1.cn > a ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['body > div.qyer_head_crumbg > div > span:nth-child(1) > a ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['body > div.qyer_head_crumbg > div > span:nth-child(3) > a ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['body > div.qyer_head_crumbg > div > span:nth-child(5) > a ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['body > div.qyer_head_crumbg > div > span:nth-child(7) > a ::text'])
        return item

    def spider_16(self,item,sel):
        #http://z.qyer.com/deal/70527/
        # 标题
        item['field1'] = self.get_info(sel,['body > div.lmMain > div.grand-title.clearfix > div.title-text > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['body > div.lmMain > div.grand-title.clearfix > div.normal-price > p.after-price > em ::text'])
        return item

    def spider_17(self,item,sel):
        #https://pkpr3.package.qunar.com/user/detail.jsp?id=3436467192
        # 标题
        item['field1'] = self.get_info(sel,['#page-root > div.wrap > div.top-mod.clrfix > div.summary > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#page-root > div.wrap > div.top-mod.clrfix > div.summary > div.price-info > div.price-main > span.number > var ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#page-root > div.page-nav > div.b_crumbs > div > a:nth-child(3) > h1 ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#page-root > div.page-nav > div.b_crumbs > div > a:nth-child(5) > h1 ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#page-root > div.page-nav > div.b_crumbs > div > a:nth-child(7) > h1 ::text'])
        return item

    def spider_18(self,item,sel):
        #https://items.fliggy.com/item.htm?id=42015390844
        # 标题
        item['field1'] = self.get_info(sel,['#J_PropertyWrap > div.detail-hd > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#J_Price > span ::text'])
        return item

    def spider_19(self,item,sel):
        #http://hotels.ctrip.com/international/996322.html
        # 标题
        item['field1'] = self.get_info(sel,['#aspnetForm > div.cont > div:nth-child(3) > div.cont_main > div > div > div:nth-child(1) > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#detail_price > span.price ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#aspnetForm > div.cont > div.path_bar2 > div:nth-child(2) > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#lnkCountryName ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#lnkCityName ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['#aspnetForm > div.cont > div.path_bar2 > div:nth-child(2) > a:nth-child(4) ::text'])
        # 分类5
        item['field7'] = self.get_info(sel,['#LocationSeoUrl ::text'])
        return item


    def spider_20(self,item,sel):
        #http://hotels.ctrip.com/apartment/2998523.html
        # 标题
        item['field1'] = self.get_info(sel,['#aspnetForm > div.bg_white.J_banners_bg_white.J_tabHeightConShift_0 > div > div > div.inn_infos_hd > div > h2 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#aspnetForm > div.bg_white.J_banners_bg_white.J_tabHeightConShift_0 > div > div > div.inn_infos_hd > div > div.inn_infos_price.J_inn_infos_price > div.inn_infos_rmb > span ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#aspnetForm > div:nth-child(30) > div > div.inn_crumbs_links > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#aspnetForm > div:nth-child(30) > div > div.inn_crumbs_links > a:nth-child(2) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['#aspnetForm > div:nth-child(30) > div > div.inn_crumbs_links > a:nth-child(3) ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['#aspnetForm > div:nth-child(30) > div > div.inn_crumbs_links > a:nth-child(4) ::text'])
        return item

    def spider_21(self,item,sel):
        #http://taocan.ctrip.com/freetravel/p5267443s2.html?kwd=大阪
        # 标题
        item['field1'] = self.get_info(sel,['#aspnetForm > div.vacation_bd.new_detail_cont > div.detail_main_wrap.basefix > div.main_right.mice_in_bottom.right_forward > div > div.detail_main_title > h2 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#js-product-min-price ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#aspnetForm > div.vacation_bd.new_detail_cont > div.crumbs > a:nth-child(3) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#aspnetForm > div.vacation_bd.new_detail_cont > div.crumbs > a:nth-child(4) ::text'])
        return item


    def spider_22(self,item,sel):
        #http://vacations.ctrip.com/grouptravel/p3634863s28.html
        # 标题
        item['field1'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.detail_main_wrap.basefix > div.main_right_col.mice_in_bottom_col > div.product_scroll_wrap.new_scroll_wrap > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#J_total_price ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > div > a:nth-child(2) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > div > a:nth-child(3) ::text'])
        return item


    def spider_23(self,item,sel):
        #http://cruise.ctrip.com/c/4800.html
        # 标题
        item['field1'] = self.get_info(sel,['body > div.cru_bd > div.detail_main_wrap > div.detail_main > div.main_right > h2 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#SailingPriceInfo > div.detail_price_box > div > div.detail_price > span > span ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['body > div.cru_bd > div.crumbs > a:nth-child(1) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['body > div.cru_bd > div.crumbs > a:nth-child(2) ::text'])
        # 分类3
        item['field5'] = self.get_info(sel,['body > div.cru_bd > div.crumbs > a:nth-child(3) ::text'])
        # 分类4
        item['field6'] = self.get_info(sel,['body > div.cru_bd > div.crumbs > h1 ::text'])
        return item

    def spider_24(self,item,sel):
        #http://vacations.ctrip.com/dingzhi/p2626153s28.html
        # 标题
        item['field1'] = self.get_info(sel,['#ProductTitle ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#customPrice > span ::text'])
        return item

    def spider_25(self,item,sel):
        #http://vacations.ctrip.com/youxue/p15176161s28.html
        # 标题
        item['field1'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.detail_main_wrap.basefix > div.main_right_col.mice_in_bottom_col > div.product_scroll_wrap.new_scroll_wrap > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#J_total_price ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > div > a:nth-child(3) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > div > a:nth-child(4) ::text'])
        return item

    def spider_26(self,item,sel):
        #http://vacations.ctrip.com/visa/p1804703s28.html
        # 标题
        item['field1'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.visa_main_mod.basefix > div.visa_main_article > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#detail_target > strong ::text'])
        # 分类1
        item['field3'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > a:nth-child(2) ::text'])
        # 分类2
        item['field4'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > a:nth-child(3) ::text'])
        return item

    def spider_27(self,item,sel):
        #http://www.hhtravel.com/product116170d319s28
        # 标题
        item['field1'] = self.get_info(sel,['body > div.wrap > div.container_box > div.goods_box > div.goods_headline > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['body > div.wrap > div.container_box > div.goods_box > div.intro_box > div.price_box > div.price > strong ::text'])
        return item

    def spider_28(self,item,sel):
        #http://vacations.ctrip.com/insurance/172
        # 标题
        item['field1'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.insure_intro.basefix.insure_newdetail > div.insure_info > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#js_insure_pricenum ::text'])
        # 分类1
        item['field3'] = u'旅游保险'
        # 分类2
        item['field4'] = self.get_info(sel,['#base_bd > div.vacation_bd > div.crumbs > a:nth-child(3) ::text'])
        return item

    def spider_29(self,item,sel):
        #http://flights.ctrip.com/international/FlightResult.aspx?flighttype=D&DCity=CTU&ACity=LED&relddate=2017-5-26%200:00:00&relrdate=2017-5-30%200:00:00&airline=HU&OnlyPrice=1#ctm_ref=fli_hp_rts_def_p_1
        # 标题
        item['field1'] = self.get_info(sel,['#ctl00_Head1 > title ::text'])
        # 分类1
        item['field3']=u'国际机票'
        return item

    def spider_30(self,item,sel):
        #http://rails.ctrip.com/passdetailsv2/101102
        # 标题
        item['field1'] = self.get_info(sel,['#secondpassName ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#price_area ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['#mainbody > div.base_bd > div.crumbs > a:nth-child(2) ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['#mainbody > div.base_bd > div.crumbs > a:nth-child(3) ::text'])
        # 分类3
        item['field5']=self.get_info(sel,['#mainbody > div.base_bd > div.crumbs > span:nth-child(4) ::text'])
        return item

    def spider_31(self,item,sel):
        #http://piao.ctrip.com/dest/t13444.html
        # 标题
        item['field1'] = self.get_info(sel,['#media-wrapper > div.media-right > h2 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#media-wrapper > div.media-price > div > span ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['#main-nav > a:nth-child(2) ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['#main-nav > h1 ::text'])
        return item


    def spider_32(self,item,sel):
        #http://huodong.ctrip.com/activity/4794625.html
        # 标题
        item['field1'] = self.get_info(sel,['#base_bd > div.bg_miancolor > div > div.detail_main_wrap.basefix > div.detail_media_right > div.detail_media_info > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['#base_bd > div.bg_miancolor > div > div.detail_main_wrap.basefix > div.detail_media_right > div.detail_book > span > strong ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['#activityLink ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['#cityActivityLink ::text'])
        return item

    def spider_33(self,item,sel):
        #http://you.ctrip.com/sight/macau39/3400.html
        # 标题
        item['field1'] = self.get_info(sel,['body > div.content.cf > div.dest_toptitle.detail_tt > div > div.f_left > h1 > a ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['body > div.content.cf > div.breadbar_v1.cf > ul > li:nth-child(3) > a ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['body > div.content.cf > div.breadbar_v1.cf > ul > li:nth-child(4) > a ::text'])
        return item

    def spider_34(self,item,sel):
        #http://g.ctrip.com/merchant/detail/9216
        # 标题
        item['field1'] = self.get_info(sel,['body > div.shop_list.merchant > div.merchant_name > div > div.merchant_nameL > h2 ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['body > div.shop_list.merchant > div.shop_address.clear_both > div > div.address_L > a ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['body > div.shop_list.merchant > div.shop_address.clear_both > div > div.address_L > a:nth-child(2) ::text'])
        # 分类3
        item['field5']=self.get_info(sel,['body > div.shop_list.merchant > div.shop_address.clear_both > div > div.address_L > a:nth-child(3) ::text'])
        return item

    def spider_35(self,item,sel):
        #http://www.mafengwo.cn/travel-scenic-spot/mafengwo/16134.html
        # 标题
        item['field1'] = self.get_info(sel,['#container > div.row.row-placeTop.row-bg > div > div.title > h1 ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['#container > div.row.row-placeTop.row-bg > div > div.crumb > div:nth-child(2) > div > span > a ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['#container > div.row.row-placeTop.row-bg > div > div.crumb > div:nth-child(3) > div > span > a ::text'])
        # 分类3
        item['field5']=self.get_info(sel,['#container > div.row.row-placeTop.row-bg > div > div.crumb > div.item.cur > strong ::text'])
        return item

    def spider_36(self,item,sel):
        #http://www.mafengwo.cn/gonglve/mdd-10027.html
        # 标题
        item['field1'] = self.get_info(sel,['body > div.wrapper > div.middle_de > h1 ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['body > div.wrapper > div.site_nav > div > a:nth-child(2) ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['body > div.wrapper > div.site_nav > div > h1 ::text'])
        return item


    def spider_37(self,item,sel):
        #http://www.mafengwo.cn/sales/2178710.html
        # 标题
        item['field1'] = self.get_info(sel,['body > div.container > div.wrapper > div.sales-intro.clearfix > div.intro-r > div.sales-title > h1 ::text'])
        # 价格
        item['field2'] = self.get_info(sel,['body > div.container > div.wrapper > div.sales-intro.clearfix > div.intro-r > div.price-panel.clearfix > ul > li.item-price > strong ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['body > div.container > div.wrapper > div.crumb > div:nth-child(2) > div > span > a ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['body > div.container > div.wrapper > div.crumb > a ::text'])
        return item

    def spider_38(self,item,sel):
        #http://www.mafengwo.cn/hotel/84734.html#checkin=2017-05-27&checkout=2017-05-28
        # 标题
        item['field1'] = self.get_info(sel,['body > div:nth-child(2) > div.hotel-intro > div.intro-hd > div.main-title > h1 ::text'])
        # 分类1
        item['field3']=self.get_info(sel,['#_j_crumb > div.crumb > div:nth-child(3) > div > span > a ::text'])
        # 分类2
        item['field4']=self.get_info(sel,['#_j_crumb > div.crumb > div:nth-child(4) > a ::text'])
        return item

    def spider_39(self,item,sel):
        #https://zh.airbnb.com/rooms/13540710
        # 标题
        item['field1'] = self.get_info(sel,['#listing_name ::text'])
        return item




