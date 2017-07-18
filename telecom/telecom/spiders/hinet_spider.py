
import scrapy
import codecs
from telecom.items import HinetStoreItem
import random
from telecom.security.gmaps import getXY

class HinetSpider(scrapy.Spider):
    name = "hinet"
    
    # custom_settings = {
    #     'DOWNLOAD_DELAY' : 1+ random.random() * random.randint(0,2),
    # }

    townCodes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                 '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    counCodes = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    urls = []

    for counCode in counCodes:
        for townCode in townCodes:
            urls.append('http://www.cht.com.tw/portal/Location_query?method=queryData&counCode=' +
                        counCode + '&townCode=' + townCode + '&keyword=',)

    start_urls = urls


    def parse(self, response):
        county = response.url.split("=")[2][:1]
        town = response.url.split("=")[3][:2]

        result = response.xpath(
            './/div[contains(@class, "services-result")]')
        length = len(result.css('h4::text').re('\w+'))

        # for tables in result:
        for i in range(length):
            item = HinetStoreItem()
            item['code'] = county + town
            item['storeType'] = result.css('h4::text').re('\w+')[i]
            item['name'] = result.css('h5::text').re('\D[\w\D]+')[i]
            address = result.xpath(
                '//td[contains(@class,"address")]/text()').re('[^\d\s]+[\w]+\-?\w+\D?\w+')[i]
            item['address'] =  address
            item['lat'] = getXY(address)[0] 
            item['lng'] = getXY(address)[1]
            yield item
