# -*- coding:utf8 -*-

import requests
import jieba

city_list = ['北京','上海','广州','深圳','宁波','武汉','重庆',
             '成都','沈阳','南京','杭州','长春','常州','大连',
             '东莞','福州','青岛','石家庄','天津','太原','西安',
             '无锡','厦门','珠海','长沙','苏州','金华','佛山',
             '济南','泉州','嘉兴','西宁','惠州','温州','中山',
             '合肥','乌鲁木齐','台州','绍兴','昆明']


KEY = 'key=9813343e8373efb0ceb3380b07094f8a'
WEATHER_URL = 'http://restapi.amap.com/v3/weather/weatherInfo?'
TRAFFIC_URL = 'http://restapi.amap.com/v3/traffic/status/road?'

def reader(name):

    name = format_input(name)
    if name:
        w_url = WEATHER_URL + KEY + '&city=' + name
        print(w_url)
        ret_content = requests.get(w_url)
        content = ret_content.json()
        print(content)
        '''
        winddirection 西北
        adcode 城市编码
        temperature 温度
        humidity 湿度
        windpower 风力
        weather 天气
        reporttime 时间
        city 城市
        province 省份
        '''
        if content['lives']:
            ret = '城市：'+content['lives'][0]['city'] + '\n'+\
                  '温度：'+content['lives'][0]['temperature']+'\n'+\
                  '湿度：'+content['lives'][0]['humidity']+'\n'+ \
                  '风力：' + content['lives'][0]['windpower'] + '\n' + \
                  '风向：' + content['lives'][0]['winddirection'] + '\n' + \
                  '时间：' + content['lives'][0]['reporttime'] + '\n'
            #url2 = URL + '&name=' + name + '&adcode=210100'  + '&' + KEY
        #print(url2)
        #content2 = requests.get(url2)
        #print(content2.text)
            return ret
        else:
            return '暂无法处理'
    else:
        return '暂无法处理'




def format_input(content):
    city = ''
    seg_list = jieba.cut(content)# 默认是精确模式
    for city in seg_list:
        print(city)

        if city in city_list:
            print('找到城市：'+city)
            return city,seg_list.__next__()
        else:
            print('您所在城市暂不支持查询！')

    return None





if __name__ == '__main__':
    reader('北京')