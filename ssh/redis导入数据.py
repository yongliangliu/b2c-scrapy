#coding=utf-8
import redis

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
key_name="market_b2c"
p=r.pipeline()

for n in range(100):
    p.lpush(key_name,'http://product.suning.com/0000000000/172519947.html')
p.execute()



# for n in f.readlines():
# 	print n.strip()
# 	r.lpush(key_name,n.strip())

# for n in range(100):

# 	# a=r.lpush(key_name,'http://www.tuniu.com/tours/210328975')
# 	url='http://www.tuniu.com/visa/visa_'+str(210423750+n)
# 	r.lpush(key_name,url)
# 	print url


# print r.llen(key_name)
# print r.rpop(key_name)
# for n in range(100):


# 	a=r.sadd(key_name,'http://item.jd.com/'+str(n+10000)+'.html')
# 	print a
# # sscan(self, name, cursor=0, match=None, count=None):

# a=r.sscan('myspider:sn',cursor=0,count=10)
# print a

# a=r.rpop(key_name)
# print a
# key_name="myspider:start_urls7"
# p=r.pipeline()
# f = open("/Users/yongliangliu/Desktop/url.txt", "r")
# for n in f.readlines():
# 	n=n.strip()
# 	if p.exists(n):
# 		print n
# 		pass
# 	else:
# 		p.lpush(key_name,n)
# p.execute()




