#!/usr/bin/python #coding: utf-8 

from scrapy.utils.project import get_project_settings
import random,base64
from scrapy.conf import settings
from user_agent import generate_user_agent

class ProcessHeaderMidware():
    """process request add request info"""

    def process_request(self, request, spider):
        ua = generate_user_agent()
        if ua:
            request.headers['User-Agent'] = ua

            # request.headers['Cookie']="tuniu_partner=MTAwLDAsLDI2OWJhMjJhNDAxOWQyNDRjYzNkMGU4ODZkMjQ1NGFk; _tacau=MCxmMjI4N2QwZC04OTMxLTc4M2ItNTZkMi1iMzY1MWYyNzNjNzQs; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; hotel_user_token=47CC2C03F521C2C7DBE4D703DDCAAEA1; global_hotel_view_history_new=D14667E2-C2B8-95D6-A113-B6CCE0CCA853; rg_entrance=010000%2F003001%2F000013%2F000000; OLBSESSID=3s6sqhmtj3ihmkmtru72oudmd0; _tacc=1; fp_ver=3.4.2; BSFIT_DEVICEID=c5264ec4110649c58ebc3078de147888; BSFIT_TRACEID=58fd521363a816df84644db4; BSFIT_EXPIRATION=1495464547634; _taca=1492572345242.1492996626071.1492999320161.5; BSFIT_OkLJUJ=GFLJ8ZVACA9XWVKQ; visit_history=210328932%2C210328975%2C6304261%2C6321206%2C210328902%2C6281359%2C; PageSwitch=1%2C213612736; _tact=NTZhOWI4OTUtOTM2NC0wNzlkLTRmYTctZjYzNDNhNGMwMzMy; _tacb=NTkwYWY0YzYtZjEwZC1kNDRjLTAzMDctMDgxYTg3OTNhNzhk; __utma=1.1490651356.1492572271.1492741666.1492996287.4; __utmb=1.6.10.1492996287; __utmc=1; __utmz=1.1492572271.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tuniuuser_citycode=MzQwMg%3D%3D; _pzfxuvpc=1492572411299%7C1386677507146266063%7C31%7C1493000886015%7C5%7C9678195002111847133%7C1345632056121414887; _pzfxsvpc=1345632056121414887%7C1492998447213%7C9%7C; connect.sid=s%3AVEXdTWoLSUUi1K6HP6b5ME3AkGJ34697.JhLBW0DALZZxswmPiCBPkQ67oDgW1PnSgTBEuOL5TxM; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999"



class ProxyMiddleware():
    def process_request(self, request, spider):
        proxy = random.choice(settings.get('PROXIES'))
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print "**************ProxyMiddleware have pass************" + proxy['ip_port']
        else:
            print "**************ProxyMiddleware no pass************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']


class IPProxyMiddleware():
    def process_request(self, request, spider):
        # bindaddress = random.choice(settings.get('BindAddress'))
        bindaddress=('0.0.0.0',0)

        print "**************ProxyMiddleware no pass************" + bindaddress[0]
        request.meta['bindaddress'] = bindaddress




