# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:14:52 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量

#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量
time=data['list'][0]['dt_txt']
name=data['city']['name']
temp=data['list'][0]['main']['temp']
wea=data['list'][0]['weather'][0]['description']
pre=data['list'][0]['main']['pressure']
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][0]['dt_txt']
name=data['city']['name']
temp=data['list'][0]['main']['temp']
wea=data['list'][0]['weather'][0]['main']
pre=data['list'][0]['main']['pressure']
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][2]['dt_txt']
name=data['city']['name']
temp=data['list'][2]['main']['temp']
wea=data['list'][2]['weather'][0]['description']
pre=data['list'][2]['main']['pressure']
temp_max=data['list'][2]['main']['temp_max']
temp_min=data['list'][2]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][2]['dt_txt']
name=data['city']['name']
temp=data['list'][2]['main']['temp']
wea=data['list'][2]['weather'][0]['main']
pre=data['list'][2]['main']['pressure']
temp_max=data['list'][2]['main']['temp_max']
temp_min=data['list'][2]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][4]['dt_txt']
name=data['city']['name']
temp=data['list'][4]['main']['temp']
wea=data['list'][4]['weather'][0]['description']
pre=data['list'][4]['main']['pressure']
temp_max=data['list'][4]['main']['temp_max']
temp_min=data['list'][4]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][4]['dt_txt']
name=data['city']['name']
temp=data['list'][4]['main']['temp']
wea=data['list'][4]['weather'][0]['main']
pre=data['list'][4]['main']['pressure']
temp_max=data['list'][4]['main']['temp_max']
temp_min=data['list'][4]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
print('2018-06-21有持续小雨，记得带伞')

time=data['list'][8]['dt_txt']
name=data['city']['name']
temp=data['list'][8]['main']['temp']
wea=data['list'][8]['weather'][0]['description']
pre=data['list'][8]['main']['pressure']
temp_max=data['list'][8]['main']['temp_max']
temp_min=data['list'][8]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][8]['dt_txt']
name=data['city']['name']
temp=data['list'][8]['main']['temp']
wea=data['list'][8]['weather'][0]['main']
pre=data['list'][8]['main']['pressure']
temp_max=data['list'][8]['main']['temp_max']
temp_min=data['list'][8]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][10]['dt_txt']
name=data['city']['name']
temp=data['list'][10]['main']['temp']
wea=data['list'][10]['weather'][0]['description']
pre=data['list'][10]['main']['pressure']
temp_max=data['list'][10]['main']['temp_max']
temp_min=data['list'][10]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][10]['dt_txt']
name=data['city']['name']
temp=data['list'][10]['main']['temp']
wea=data['list'][10]['weather'][0]['main']
pre=data['list'][10]['main']['pressure']
temp_max=data['list'][10]['main']['temp_max']
temp_min=data['list'][10]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][12]['dt_txt']
name=data['city']['name']
temp=data['list'][12]['main']['temp']
wea=data['list'][12]['weather'][0]['description']
pre=data['list'][12]['main']['pressure']
temp_max=data['list'][12]['main']['temp_max']
temp_min=data['list'][12]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][12]['dt_txt']
name=data['city']['name']
temp=data['list'][12]['main']['temp']
wea=data['list'][12]['weather'][0]['main']
pre=data['list'][12]['main']['pressure']
temp_max=data['list'][12]['main']['temp_max']
temp_min=data['list'][12]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
print('2018-06-22小雨转大雨，记得带伞，增加衣物')

time=data['list'][16]['dt_txt']
name=data['city']['name']
temp=data['list'][16]['main']['temp']
wea=data['list'][16]['weather'][0]['description']
pre=data['list'][16]['main']['pressure']
temp_max=data['list'][16]['main']['temp_max']
temp_min=data['list'][16]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][16]['dt_txt']
name=data['city']['name']
temp=data['list'][16]['main']['temp']
wea=data['list'][16]['weather'][0]['main']
pre=data['list'][16]['main']['pressure']
temp_max=data['list'][16]['main']['temp_max']
temp_min=data['list'][16]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][18]['dt_txt']
name=data['city']['name']
temp=data['list'][18]['main']['temp']
wea=data['list'][18]['weather'][0]['description']
pre=data['list'][18]['main']['pressure']
temp_max=data['list'][18]['main']['temp_max']
temp_min=data['list'][18]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][18]['dt_txt']
name=data['city']['name']
temp=data['list'][18]['main']['temp']
wea=data['list'][18]['weather'][0]['main']
pre=data['list'][18]['main']['pressure']
temp_max=data['list'][18]['main']['temp_max']
temp_min=data['list'][18]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][20]['dt_txt']
name=data['city']['name']
temp=data['list'][20]['main']['temp']
wea=data['list'][20]['weather'][0]['description']
pre=data['list'][20]['main']['pressure']
temp_max=data['list'][20]['main']['temp_max']
temp_min=data['list'][20]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][20]['dt_txt']
name=data['city']['name']
temp=data['list'][20]['main']['temp']
wea=data['list'][20]['weather'][0]['main']
pre=data['list'][20]['main']['pressure']
temp_max=data['list'][20]['main']['temp_max']
temp_min=data['list'][20]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
print('2018-06-23有持续小雨，记得带伞')

time=data['list'][24]['dt_txt']
name=data['city']['name']
temp=data['list'][24]['main']['temp']
wea=data['list'][24]['weather'][0]['description']
pre=data['list'][24]['main']['pressure']
temp_max=data['list'][24]['main']['temp_max']
temp_min=data['list'][24]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][24]['dt_txt']
name=data['city']['name']
temp=data['list'][24]['main']['temp']
wea=data['list'][24]['weather'][0]['main']
pre=data['list'][24]['main']['pressure']
temp_max=data['list'][24]['main']['temp_max']
temp_min=data['list'][24]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][26]['dt_txt']
name=data['city']['name']
temp=data['list'][26]['main']['temp']
wea=data['list'][26]['weather'][0]['description']
pre=data['list'][26]['main']['pressure']
temp_max=data['list'][26]['main']['temp_max']
temp_min=data['list'][26]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][26]['dt_txt']
name=data['city']['name']
temp=data['list'][26]['main']['temp']
wea=data['list'][26]['weather'][0]['main']
pre=data['list'][26]['main']['pressure']
temp_max=data['list'][26]['main']['temp_max']
temp_min=data['list'][26]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][28]['dt_txt']
name=data['city']['name']
temp=data['list'][28]['main']['temp']
wea=data['list'][28]['weather'][0]['description']
pre=data['list'][28]['main']['pressure']
temp_max=data['list'][28]['main']['temp_max']
temp_min=data['list'][28]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][28]['dt_txt']
name=data['city']['name']
temp=data['list'][28]['main']['temp']
wea=data['list'][28]['weather'][0]['main']
pre=data['list'][28]['main']['pressure']
temp_max=data['list'][28]['main']['temp_max']
temp_min=data['list'][28]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
print('2018-06-24中雨转多云，可以适当增减衣物')

time=data['list'][32]['dt_txt']
name=data['city']['name']
temp=data['list'][32]['main']['temp']
wea=data['list'][32]['weather'][0]['description']
pre=data['list'][32]['main']['pressure']
temp_max=data['list'][32]['main']['temp_max']
temp_min=data['list'][32]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][32]['dt_txt']
name=data['city']['name']
temp=data['list'][32]['main']['temp']
wea=data['list'][32]['weather'][0]['main']
pre=data['list'][32]['main']['pressure']
temp_max=data['list'][32]['main']['temp_max']
temp_min=data['list'][32]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][34]['dt_txt']
name=data['city']['name']
temp=data['list'][34]['main']['temp']
wea=data['list'][34]['weather'][0]['description']
pre=data['list'][34]['main']['pressure']
temp_max=data['list'][34]['main']['temp_max']
temp_min=data['list'][34]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][34]['dt_txt']
name=data['city']['name']
temp=data['list'][34]['main']['temp']
wea=data['list'][34]['weather'][0]['main']
pre=data['list'][34]['main']['pressure']
temp_max=data['list'][34]['main']['temp_max']
temp_min=data['list'][34]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))

time=data['list'][36]['dt_txt']
name=data['city']['name']
temp=data['list'][36]['main']['temp']
wea=data['list'][36]['weather'][0]['description']
pre=data['list'][36]['main']['pressure']
temp_max=data['list'][36]['main']['temp_max']
temp_min=data['list'][36]['main']['temp_min']
print('{},城市{}，温度是:{},天气情况是:{},气压是:{},最高温度:{},最低温度:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
time=data['list'][36]['dt_txt']
name=data['city']['name']
temp=data['list'][36]['main']['temp']
wea=data['list'][36]['weather'][0]['main']
pre=data['list'][36]['main']['pressure']
temp_max=data['list'][36]['main']['temp_max']
temp_min=data['list'][36]['main']['temp_min']
print('time:{},Please enter the name of the city to be inquired：{},temperature:{},the weather is:{},pressure:{},maximum temperature:{},minimum temperature:{}'.format(time,name,temp,wea,pre,temp_max,temp_min))
print('2018-06-25多云，适合外出')