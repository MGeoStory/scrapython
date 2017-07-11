import scrapy
from telecom.items import TFNStoreItem
import json


class TFN_Spider(scrapy.Spider):
    name = 'tfn'
    def start_requests(self):
        cities = ['基隆市','台北市','新北市','宜蘭縣','新竹市','新竹縣','桃園市','苗栗縣','台中市','彰化縣','南投縣','嘉義市','嘉義縣','雲林縣','台南市','高雄市','屏東縣','台東縣','花蓮縣','金門縣','連江縣','澎湖縣','南海諸島']
        for city in cities:
            yield scrapy.Request(
                'https://www.taiwanmobile.com/cs/public/storeAction.do?method=searchLBS&city=' +
                city + '&lat=25.0462585&lng=121.5164218&searchDistance=-1',
                self.parse,
                method='POST'
            )

    def parse(self, response):
        json_respone = json.loads(response.text)
        special_stores = json_respone['specialStores']
        direct_stores = json_respone['directStores']

        length_special_stores = len(special_stores)
        for i in range(length_special_stores):
            item = TFNStoreItem()
            item['storeType'] = '特約'
            item['name'] = special_stores[i]['name']
            item['address'] = special_stores[i]['address']
            item['lat'] = special_stores[i]['geometryy']
            item['lng'] = special_stores[i]['geometryx']
            yield item
            
        # print(len(json_string))
        length_direct_stores = len(direct_stores)
        for i in range(length_direct_stores):
            item = TFNStoreItem()
            item['storeType'] = '直營'
            item['name'] = direct_stores[i]['name']
            item['address'] = direct_stores[i]['address']
            item['lat'] = direct_stores[i]['geometryy']
            item['lng'] = direct_stores[i]['geometryx']
            yield item