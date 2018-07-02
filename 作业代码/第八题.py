# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 22:07:11 2018

@author: Administrator

商品名，价格，付款，店铺名,地址




"""

f=open('./上海.csv','w')
f.write('店铺名,商品名,价格,销量,地址\n')
for i in range(0,100):
    import urllib.request as r
    url2='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=t%E6%81%A4%E7%94%B7&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E6%9D%AD%E5%B7%9E&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0&ajax=true'
    a=44*i
    url=url2.replace('0&ajax=true',str(a)+'&ajax=true')
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    l=len(data['mods']['itemlist']['data']['auctions'])
    for a in range(0,l):
        nick=data['mods']['itemlist']['data']['auctions'][a]['nick']#店铺名
        raw_title=data['mods']['itemlist']['data']['auctions'][a]['raw_title']#商品名
        view_price=data['mods']['itemlist']['data']['auctions'][a]['view_price']#价格
        view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']#销量
        item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']#地址
        f.write('{},{},{},{},{}\n'.format(nick,raw_title,view_price,view_sales,item_loc))
    print('第{}页已获取数据'.format(i+1))
f.close()
print('关键词为“t恤男”上海地区前100页数据获取完成！')









