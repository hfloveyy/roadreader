# -*- coding:utf8 -*-

import requests

city_list = ['北京','上海','广州','深圳','宁波','武汉','重庆',
             '成都','沈阳','南京','杭州','长春','常州','大连',
             '东莞','福州','青岛','石家庄','天津','太原','西安',
             '无锡','厦门','珠海','长沙','苏州','金华','佛山',
             '济南','泉州','嘉兴','西宁','惠州','温州','中山',
             '合肥','乌鲁木齐','台州','绍兴','昆明']


KEY = 'key=9813343e8373efb0ceb3380b07094f8a'
WEATHER_URL = 'http://restapi.amap.com/v3/weather/weatherInfo?'#'http://restapi.amap.com/v3/traffic/status/road?'
URL = 'http://restapi.amap.com/v3/traffic/status/road?'
def reader(name):
    '''
    if name not in city_list:
        return '您所在城市暂不能查询'
    '''

    url = WEATHER_URL + KEY + '&city=' + name
    print(url)
    content = requests.get(url)
    print(content.json())
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
    #url2 = URL + '&name=' + name + '&adcode=210100'  + '&' + KEY
    #print(url2)
    #content2 = requests.get(url2)
    #print(content2.text)
    return content.json()['lives'][0]['city']


if __name__ == '__main__':
    reader('哈尔滨')