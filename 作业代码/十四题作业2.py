# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:10:48 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
f=open('./a.txt','a')
f.write(d+"\n")
f.close()
for i in range(len(a)):
   data='id={}&type=2&city=33&state=1'.format(a[i])
   req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
   d=r.urlopen(req).read().decode('utf-8','ignore')
   f=open('./a.txt','a')
   f.write(d+"\n")
f.close()

f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
f.close()    
m=[]
import urllib.request as r    
for i in range(1985,2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=31&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=34&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))

#再次检验是否有错
for i in range(2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=31&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))

f=open('./上海文科.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()   

f=open('./all_school.txt','r',encoding='utf-8')
s=f.read()
import re
s1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(s)
f.close()    
m=[]
import urllib.request as r    
for i in range(0,2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=33&state=1'.format(s1[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=33&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))

#再次检验是否有错
for i in range(0,2300):
    a=m[i]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=33&state=1'.format(s1[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        a=i
        print('{}次输出成功'.format(a))

f=open('./浙江文科1.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close()    
    
  

m=[]
import urllib.request as r    
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=33&state=1'.format(a[i])
    data=data.encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    p=r.urlopen(req).read().decode('utf-8','ignore')
    m.append(p)
    b=m[i]
    if b.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=33&state=1'.format(a[i])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        p=r.urlopen(req).read().decode('utf-8','ignore')
        m[i]=p
    else:
        b=i
        print('{}次输出成功'.format(b))
        continue

f=open('./修改华东地区汇总.txt','w',encoding='utf-8')
for i in range(len(m)):
    p=m[i]
    f.write(p+"\n")
f.close() 

m=[]
import urllib.request as r
url='file:./浙江理科.txt'
data=r.urlopen(url).read().decode('utf-8')
data=data.split()
import json
for i in range(2300):
    a=json.loads(data[i])
    m.append(a)

n=0
for j in range(2300):
    b1=m1[j]['data']
    b2=m1[j]['status']
    if b2==0:
        print('第{}的学校不在该地区招生'.format(j))
    else:
        b3=m1[j]['data'][0]['subject']
        b4=m1[j]['data'][0]['school']
        print('采取-{}-{}类-的人数'.format(b4,b3))
        for k in range(len(b1)):
            b4=m1[j]['data'][k]['plan']
            b6=m1[j]['data'][0]['school']
            b4=int(b4)
            n=n+b4
            print(n)
        print('{}采取完成'.format(b6))


ls1=['上海理科','上海文科','江苏理科','江苏文科','浙江理科','浙江文科','安徽理科','安徽文科']
b=0
for i in range(len(m)):
    d=0
    for x in range(len(m[i])):
        if int(m[i]['status'])==1:
            l2=len(m[i]['data'])
            for c in range(l2):
              
                d=d+int(m[i]['data'][c]['plan'])
                print('江苏的招生人数是:{}'.format(d))
print('华东地区文理科的招生人数是:{}'.format(b))

n=0
for i in range(2300):
    b1=m[i]['status']
    if b1==1:
        b2=m[i]['data']
        for j in range(len(b2)):
            b3=m[i]['data'][j]['plan']
            b3=int(b3)
            n=n+b3
            print('现在招生人数为{}'.format(n))
m=[]
import urllib.request as r
url='file:./上海文科.txt'
data=r.urlopen(url).read().decode('utf-8')
data=data.split('\n')
import json
for i in range(2300):
    a=json.loads(data[i])
    m.append(a)
c=0
for i in range(len(m)):
    b1=m[i]['status']
    b2=m[i]['data'][0]['city'] 
    if b1==1:
        b4=m[i]['data']
        for j in range(len(b4)):
                b3=m[i]['data'][j]['plan']
                b3=int(b3)
                c=c+b3
print('全国对于{}的招生总人数为{}'.format(b2,c))

f=open('./修改华东地区汇总.txt','a',encoding='utf-8')
f1=open('./上海文科.txt','r',encoding='utf-8')
d1=f1.read() 
f2=open('./上海理科.txt','r',encoding='utf-8')
d2=f2.read()  
f3=open('./安徽 文.txt','r',encoding='utf-8')
d3=f3.read()  
f4=open('./安徽理科.txt','r',encoding='utf-8') 
d4=f4.read() 
f5=open('./江苏文科.txt','r',encoding='utf-8')  
d5=f5.read()
f6=open('./江苏理科.txt','r',encoding='utf-8')  
d6=f6.read()
f7=open('./浙江文科1.txt','r',encoding='utf-8')  
d7=f7.read()
f8=open('./浙江理科.txt','r',encoding='utf-8')  
d8=f8.read()
f.write('{}{}{}{}{}{}{}{}\n'.format(d1,d2,d3,d4,d5,d6,d7,d8))
f.close()














