import scrapy
from telecom.items import FETStoreItem
import json
import random


class FET_Spider(scrapy.Spider):
    # response.xpath('//*[@id="wrapper"]/section/div[2]/div/div/div/div/div/d
    # ...: iv[1]/div[2]/input[1]/@value').re('\w+') to get counties

    name = 'fet'

    def start_requests(self):
        cities = [
            '桃園市',
            '彰化縣',
            '台北市',
            '基隆市',
            '新北市',
            '宜蘭縣',
            '新竹市',
            '新竹縣',
            '苗栗縣',
            '台中市',
            '南投縣',
            '嘉義市',
            '嘉義縣',
            '雲林縣',
            '台南市',
            '高雄市',
            '澎湖縣',
            '金門縣',
            '屏東縣',
            '台東縣',
            '花蓮縣',
        ]
        areas = [
            ['桃園區', '中壢區', '楊梅區', '八德區', '蘆竹區', '龍潭區',
                '龜山區', '平鎮區', '大溪區', '觀音區', '大園區', '新屋區'],
            ['彰化市', '花壇鄉', '鹿港鎮', '和美鎮', '伸港鄉', '員林鎮', '社頭鄉', '永靖鄉',
                '埔心鄉', '溪湖鎮', '大村鄉', '田中鎮', '北斗鎮', '埤頭鄉', '二林鎮'],
            ['中正區', '大同區', '中山區', '松山區', '大安區', '萬華區',
                '信義區', '士林區', '北投區', '內湖區', '南港區', '文山區'],
            ['仁愛區', '信義區', '中正區', '中山區', '安樂區', '暖暖區', '七堵區'],
            ['金山區', '板橋區', '汐止區', '深坑區', '瑞芳區', '新店區', '永和區', '中和區', '土城區', '三峽區',
                '樹林區', '鶯歌區', '三重區', '新莊區', '泰山區', '林口區', '蘆洲區', '五股區', '八里區', '淡水區'],
            ['宜蘭市', '礁溪鄉', '羅東鎮', '五結鄉', '冬山鄉', '蘇澳鎮'],
            ['北區', '東區', '香山區'],
            ['竹北市', '湖口鄉', '新豐鄉', '新埔鎮', '關西鎮', '竹東鎮'],
            ['竹南鎮', '頭份鎮', '後龍鎮', '通霄鎮', '苑裡鎮', '苗栗市', '公館鄉'],
            ['中區', '東區', '南區', '西區', '北區', '北屯區', '西屯區', '南屯區', '太平區', '大里區', '霧峰區', '烏日區', '豐原區',
                '后里區', '東勢區', '新社區', '潭子區', '大雅區', '神岡區', '大肚區', '沙鹿區', '龍井區', '梧棲區', '清水區', '大甲區', '外埔區'],
            ['南投市', '草屯鎮', '埔里鎮', '名間鄉', '水里鄉', '竹山鎮'],
            ['西區', '東區'],
            ['竹崎鄉', '水上鄉', '太保市', '朴子市', '新港鄉', '民雄鄉', '大林鎮', '義竹鄉', '布袋鎮'],
            ['斗南鎮', '虎尾鎮', '麥寮鄉', '斗六市', '莿桐鄉', '西螺鎮', '北港鎮'],
            ['東區', '南區', '北區', '中西區', '安平區', '安南區', '永康區', '歸仁區', '新化區', '仁德區',
                '關廟區', '麻豆區', '佳里區', '西港區', '學甲區', '新營區', '白河區', '鹽水區', '善化區', '新市區'],
            ['新興區', '前金區', '苓雅區', '鹽埕區', '鼓山區', '旗津區', '前鎮區', '楠梓區', '小港區', '左營區', '仁武區', '大社區', '岡山區', '路竹區',
                '阿蓮區', '燕巢區', '橋頭區', '梓官區', '湖內區', '鳳山區', '大寮區', '林園區', '鳥松區', '旗山區', '美濃區', '三民區', '茄萣區'],
            ['馬公市'],
            ['金城鎮'],
            ['屏東市', '里港鄉', '高樹鄉', '鹽埔鄉', '內埔鄉', '萬丹鄉',
                '潮州鎮', '林邊鄉', '東港鎮', '枋寮鄉', '恆春鎮'],
            ['台東市', '關山鎮'],
            ['花蓮市', '吉安鄉', '玉里鎮']
        ]

        # for i in range(0, 21):
        #     print(areas[i])
        #     for j in range(0, len(cities[i])):
        #         print([cities[i][j]])
        #         yield scrapy.Request(
        #             'https://ecare.fetnet.net/eServiceV3/storeSearchController/ShopCenterSearchFilter.action?_t=1499789709701&area=' +
        #             areas[i] + '&city=' + cities[i][j] + '&isAjax=true',
        #             self.parse,
        #             method='POST'
        #         )
        for i in range(0, len(cities)):
            print('===============================')
            for j in range(0, len(areas[i])):
                yield scrapy.Request(
                    'https://ecare.fetnet.net/eServiceV3/storeSearchController/ShopCenterSearchFilter.action?city=' +
                    cities[i] + '&area=' + areas[i][j],
                    self.parse,
                    method='POST'
                )
                
        custom_settings = {
            'DOWNLOAD_DELAY': random.randint(1, 10) * 0.25,
        }

    def parse(self, response):
        json_respone = json.loads(response.text)
        datas = json_respone['result']['datas']
        for i in range(len(datas)):
            item = FETStoreItem()
            # print(datas[i]['storeType'])
            item['storeType'] = datas[i]['storeType']
            item['name'] = datas[i]['storeName']
            item['address'] = datas[i]['storeAddress']
            item['lat'] = datas[i]['storeLongitude']
            item['lng'] = datas[i]['storeLatitude']
            item['city'] = datas[i]['storeCity']
            item['county'] = datas[i]['storeArea']
            yield item
        print('===============================')
