#encoding=utf-8
import jieba

city_list = ['北京','上海','广州','深圳','宁波','武汉','重庆',
             '成都','沈阳','南京','杭州','长春','常州','大连',
             '东莞','福州','青岛','石家庄','天津','太原','西安',
             '无锡','厦门','珠海','长沙','苏州','金华','佛山',
             '济南','泉州','嘉兴','西宁','惠州','温州','中山',
             '合肥','乌鲁木齐','台州','绍兴','昆明']




def format_input(content):
    seg_list = jieba.cut(content)# 默认是精确模式
    for city in seg_list:
        if city in city_list:
            print('找到城市：'+city)
            return city
        else:
            print('您所在城市暂不支持查询！')
            pass

format_input("上海香坊大街")#默认是精确模式


'''
seg_list = jieba.cut_for_search("上海市") #搜索引擎模式
print (", ".join(seg_list))
print(type(seg_list))


seg_list = jieba.cut("上海市",cut_all=True)
print("Full Mode:", "/ ".join(seg_list) )#全模式

seg_list = jieba.cut("上海",cut_all=False)
print ("Default Mode:", "/ ".join(seg_list) )#精确模式
'''