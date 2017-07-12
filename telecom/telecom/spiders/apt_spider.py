# https://www.aptg.com.tw/store/stores/district/仁愛區/基隆市

import scrapy
from telecom.items import APTStoreItem
import json
import random
import re

class APT_Spider(scrapy.Spider):

    name = 'apt'
    custom_settings = {
        'DOWNLOAD_DELAY': random.randint(1, 10) * 0.25,
    }

    def start_requests(self):
            cities = [
                '基隆市',
                '台北市',
                '新北市',
                '宜蘭縣',
                '新竹市',
                '新竹縣',
                '桃園市',
                '苗栗縣',
                '台中市',
                '彰化縣',
                '南投縣',
                '嘉義市',
                '嘉義縣',
                '雲林縣',
                '台南市',
                '高雄市',
                '屏東縣',
                '台東縣',
                '花蓮縣',
                '金門縣',
                '連江縣',
                '澎湖縣',
            ]

            list_of_county =[
                '<select name="district"><option value="仁愛區">200 仁愛區</option><option value="信義區">201 信義區</option><option value="中正區">202 中正區</option><option value="中山區">203 中山區</option><option value="安樂區">204 安樂區</option><option value="暖暖區">205 暖暖區</option><option value="七堵區">206 七堵區</option></select>',        
                '<select name="district"><option value="中正區">100 中正區</option><option value="大同區">103 大同區</option><option value="中山區">104 中山區</option><option value="松山區">105 松山區</option><option value="大安區">106 大安區</option><option value="萬華區">108 萬華區</option><option value="信義區">110 信義區</option><option value="士林區">111 士林區</option><option value="北投區">112 北投區</option><option value="內湖區">114 內湖區</option><option value="南港區">115 南港區</option><option value="文山區">116 文山區</option></select>',
                '<select name="district"><option value="萬里區">207 萬里區</option><option value="金山區">208 金山區</option><option value="板橋區">220 板橋區</option><option value="汐止區">221 汐止區</option><option value="深坑區">222 深坑區</option><option value="石碇區">223 石碇區</option><option value="瑞芳區">224 瑞芳區</option><option value="平溪區">226 平溪區</option><option value="雙溪區">227 雙溪區</option><option value="貢寮區">228 貢寮區</option><option value="新店區">231 新店區</option><option value="坪林區">232 坪林區</option><option value="烏來區">233 烏來區</option><option value="永和區">234 永和區</option><option value="中和區">235 中和區</option><option value="土城區">236 土城區</option><option value="三峽區">237 三峽區</option><option value="樹林區">238 樹林區</option><option value="鶯歌區">239 鶯歌區</option><option value="三重區">241 三重區</option><option value="新莊區">242 新莊區</option><option value="泰山區">243 泰山區</option><option value="林口區">244 林口區</option><option value="蘆洲區">247 蘆洲區</option><option value="五股區">248 五股區</option><option value="八里區">249 八里區</option><option value="淡水區">251 淡水區</option><option value="三芝區">252 三芝區</option><option value="石門區">253 石門區</option></select>',
                '<select name="district"><option value="宜蘭市">260 宜蘭市</option><option value="頭城鎮">261 頭城鎮</option><option value="礁溪鄉">262 礁溪鄉</option><option value="壯圍鄉">263 壯圍鄉</option><option value="員山鄉">264 員山鄉</option><option value="羅東鎮">265 羅東鎮</option><option value="三星鄉">266 三星鄉</option><option value="大同鄉">267 大同鄉</option><option value="五結鄉">268 五結鄉</option><option value="冬山鄉">269 冬山鄉</option><option value="蘇澳鎮">270 蘇澳鎮</option><option value="南澳鄉">272 南澳鄉</option><option value="釣魚台列嶼">290 釣魚台列嶼</option></select>',
                '<select name="district"><option value="東區">300 東區</option><option value="北區">300 北區</option><option value="香山區">300 香山區</option></select>',
                '<select name="district"><option value="竹北市">302 竹北市</option><option value="湖口鄉">303 湖口鄉</option><option value="新豐鄉">304 新豐鄉</option><option value="新埔鎮">305 新埔鎮</option><option value="關西鎮">306 關西鎮</option><option value="芎林鄉">307 芎林鄉</option><option value="寶山鄉">308 寶山鄉</option><option value="竹東鎮">310 竹東鎮</option><option value="五峰鄉">311 五峰鄉</option><option value="橫山鄉">312 橫山鄉</option><option value="尖石鄉">313 尖石鄉</option><option value="北埔鄉">314 北埔鄉</option><option value="峨嵋鄉">315 峨嵋鄉</option></select>',
                '<select name="district"><option value="中壢區">320 中壢區</option><option value="平鎮區">324 平鎮區</option><option value="龍潭區">325 龍潭區</option><option value="楊梅區">326 楊梅區</option><option value="新屋區">327 新屋區</option><option value="觀音區">328 觀音區</option><option value="桃園區">330 桃園區</option><option value="龜山區">333 龜山區</option><option value="八德區">334 八德區</option><option value="大溪區">335 大溪區</option><option value="復興區">336 復興區</option><option value="大園區">337 大園區</option><option value="蘆竹區">338 蘆竹區</option></select>',
                '<select name="district"><option value="竹南鎮">350 竹南鎮</option><option value="頭份市">351 頭份市</option><option value="三灣鄉">352 三灣鄉</option><option value="南庄鄉">353 南庄鄉</option><option value="獅潭鄉">354 獅潭鄉</option><option value="後龍鎮">356 後龍鎮</option><option value="通霄鎮">357 通霄鎮</option><option value="苑裡鎮">358 苑裡鎮</option><option value="苗栗市">360 苗栗市</option><option value="造橋鄉">361 造橋鄉</option><option value="頭屋鄉">362 頭屋鄉</option><option value="公館鄉">363 公館鄉</option><option value="大湖鄉">364 大湖鄉</option><option value="泰安鄉">365 泰安鄉</option><option value="銅鑼鄉">366 銅鑼鄉</option><option value="三義鄉">367 三義鄉</option><option value="西湖鄉">368 西湖鄉</option><option value="卓蘭鎮">369 卓蘭鎮</option></select>',
                '<select name="district"><option value="中區">400 中區</option><option value="東區">401 東區</option><option value="南區">402 南區</option><option value="西區">403 西區</option><option value="北區">404 北區</option><option value="北屯區">406 北屯區</option><option value="西屯區">407 西屯區</option><option value="南屯區">408 南屯區</option><option value="太平區">411 太平區</option><option value="大里區">412 大里區</option><option value="霧峰區">413 霧峰區</option><option value="烏日區">414 烏日區</option><option value="豐原區">420 豐原區</option><option value="后里區">421 后里區</option><option value="石岡區">422 石岡區</option><option value="東勢區">423 東勢區</option><option value="和平區">424 和平區</option><option value="新社區">426 新社區</option><option value="潭子區">427 潭子區</option><option value="大雅區">428 大雅區</option><option value="神岡區">429 神岡區</option><option value="大肚區">432 大肚區</option><option value="沙鹿區">433 沙鹿區</option><option value="龍井區">434 龍井區</option><option value="梧棲區">435 梧棲區</option><option value="清水區">436 清水區</option><option value="大甲區">437 大甲區</option><option value="外埔區">438 外埔區</option><option value="大安區">439 大安區</option></select>',
                '<select name="district"><option value="彰化市">500 彰化市</option><option value="芬園鄉">502 芬園鄉</option><option value="花壇鄉">503 花壇鄉</option><option value="秀水鄉">504 秀水鄉</option><option value="鹿港鎮">505 鹿港鎮</option><option value="福興鄉">506 福興鄉</option><option value="線西鄉">507 線西鄉</option><option value="和美鎮">508 和美鎮</option><option value="伸港鄉">509 伸港鄉</option><option value="員林市">510 員林市</option><option value="社頭鄉">511 社頭鄉</option><option value="永靖鄉">512 永靖鄉</option><option value="埔心鄉">513 埔心鄉</option><option value="溪湖鎮">514 溪湖鎮</option><option value="大村鄉">515 大村鄉</option><option value="埔鹽鄉">516 埔鹽鄉</option><option value="田中鎮">520 田中鎮</option><option value="北斗鎮">521 北斗鎮</option><option value="田尾鄉">522 田尾鄉</option><option value="埤頭鄉">523 埤頭鄉</option><option value="溪州鄉">524 溪州鄉</option><option value="竹塘鄉">525 竹塘鄉</option><option value="二林鎮">526 二林鎮</option><option value="大城鄉">527 大城鄉</option><option value="芳苑鄉">528 芳苑鄉</option><option value="二水鄉">530 二水鄉</option></select>',
                '<select name="district"><option value="南投市">540 南投市</option><option value="中寮鄉">541 中寮鄉</option><option value="草屯鎮">542 草屯鎮</option><option value="國姓鄉">544 國姓鄉</option><option value="埔里鎮">545 埔里鎮</option><option value="仁愛鄉">546 仁愛鄉</option><option value="名間鄉">551 名間鄉</option><option value="集集鎮">552 集集鎮</option><option value="水里鄉">553 水里鄉</option><option value="魚池鄉">555 魚池鄉</option><option value="信義鄉">556 信義鄉</option><option value="竹山鎮">557 竹山鎮</option><option value="鹿谷鄉">558 鹿谷鄉</option></select>',
                '<select name="district"><option value="東區">600 東區</option><option value="西區">600 西區</option></select>',
                '<select name="district"><option value="番路鄉">602 番路鄉</option><option value="梅山鄉">603 梅山鄉</option><option value="竹崎鄉">604 竹崎鄉</option><option value="阿里山">605 阿里山</option><option value="中埔鄉">606 中埔鄉</option><option value="大埔鄉">607 大埔鄉</option><option value="水上鄉">608 水上鄉</option><option value="鹿草鄉">611 鹿草鄉</option><option value="太保市">612 太保市</option><option value="朴子市">613 朴子市</option><option value="東石鄉">614 東石鄉</option><option value="六腳鄉">615 六腳鄉</option><option value="新港鄉">616 新港鄉</option><option value="民雄鄉">621 民雄鄉</option><option value="大林鎮">622 大林鎮</option><option value="溪口鄉">623 溪口鄉</option><option value="義竹鄉">624 義竹鄉</option><option value="布袋鎮">625 布袋鎮</option></select>',
                '<select name="district"><option value="斗南鎮">630 斗南鎮</option><option value="大埤鄉">631 大埤鄉</option><option value="虎尾鎮">632 虎尾鎮</option><option value="土庫鎮">633 土庫鎮</option><option value="褒忠鄉">634 褒忠鄉</option><option value="東勢鄉">635 東勢鄉</option><option value="臺西鄉">636 臺西鄉</option><option value="崙背鄉">637 崙背鄉</option><option value="麥寮鄉">638 麥寮鄉</option><option value="斗六市">640 斗六市</option><option value="林內鄉">643 林內鄉</option><option value="古坑鄉">646 古坑鄉</option><option value="莿桐鄉">647 莿桐鄉</option><option value="西螺鎮">648 西螺鎮</option><option value="二崙鄉">649 二崙鄉</option><option value="北港鎮">651 北港鎮</option><option value="水林鄉">652 水林鄉</option><option value="口湖鄉">653 口湖鄉</option><option value="四湖鄉">654 四湖鄉</option><option value="元長鄉">655 元長鄉</option></select>',
                '<select name="district"><option value="中西區">700 中西區</option><option value="東區">701 東區</option><option value="南區">702 南區</option><option value="北區">704 北區</option><option value="安平區">708 安平區</option><option value="安南區">709 安南區</option><option value="永康區">710 永康區</option><option value="歸仁區">711 歸仁區</option><option value="新化區">712 新化區</option><option value="左鎮區">713 左鎮區</option><option value="玉井區">714 玉井區</option><option value="楠西區">715 楠西區</option><option value="南化區">716 南化區</option><option value="仁德區">717 仁德區</option><option value="關廟區">718 關廟區</option><option value="龍崎區">719 龍崎區</option><option value="官田區">720 官田區</option><option value="麻豆區">721 麻豆區</option><option value="佳里區">722 佳里區</option><option value="西港區">723 西港區</option><option value="七股區">724 七股區</option><option value="將軍區">725 將軍區</option><option value="學甲區">726 學甲區</option><option value="北門區">727 北門區</option><option value="新營區">730 新營區</option><option value="後壁區">731 後壁區</option><option value="白河區">732 白河區</option><option value="東山區">733 東山區</option><option value="六甲區">734 六甲區</option><option value="下營區">735 下營區</option><option value="柳營區">736 柳營區</option><option value="鹽水區">737 鹽水區</option><option value="善化區">741 善化區</option><option value="大內區">742 大內區</option><option value="山上區">743 山上區</option><option value="新市區">744 新市區</option><option value="安定區">745 安定區</option></select>',
                '<select name="district"><option value="新興區">800 新興區</option><option value="前金區">801 前金區</option><option value="苓雅區">802 苓雅區</option><option value="鹽埕區">803 鹽埕區</option><option value="鼓山區">804 鼓山區</option><option value="旗津區">805 旗津區</option><option value="前鎮區">806 前鎮區</option><option value="三民區">807 三民區</option><option value="楠梓區">811 楠梓區</option><option value="小港區">812 小港區</option><option value="左營區">813 左營區</option><option value="仁武區">814 仁武區</option><option value="大社區">815 大社區</option><option value="東沙群島">817 東沙群島</option><option value="南沙群島">819 南沙群島</option><option value="岡山區">820 岡山區</option><option value="路竹區">821 路竹區</option><option value="阿蓮區">822 阿蓮區</option><option value="田寮區">823 田寮區</option><option value="燕巢區">824 燕巢區</option><option value="橋頭區">825 橋頭區</option><option value="梓官區">826 梓官區</option><option value="彌陀區">827 彌陀區</option><option value="永安區">828 永安區</option><option value="湖內區">829 湖內區</option><option value="鳳山區">830 鳳山區</option><option value="大寮區">831 大寮區</option><option value="林園區">832 林園區</option><option value="鳥松區">833 鳥松區</option><option value="大樹區">840 大樹區</option><option value="旗山區">842 旗山區</option><option value="美濃區">843 美濃區</option><option value="六龜區">844 六龜區</option><option value="內門區">845 內門區</option><option value="杉林區">846 杉林區</option><option value="甲仙區">847 甲仙區</option><option value="桃源區">848 桃源區</option><option value="那瑪夏區">849 那瑪夏區</option><option value="茂林區">851 茂林區</option><option value="茄萣區">852 茄萣區</option></select>',
                '<select name="district"><option value="屏東市">900 屏東市</option><option value="三地門鄉">901 三地門鄉</option><option value="霧臺鄉">902 霧臺鄉</option><option value="瑪家鄉">903 瑪家鄉</option><option value="九如鄉">904 九如鄉</option><option value="里港鄉">905 里港鄉</option><option value="高樹鄉">906 高樹鄉</option><option value="鹽埔鄉">907 鹽埔鄉</option><option value="長治鄉">908 長治鄉</option><option value="麟洛鄉">909 麟洛鄉</option><option value="竹田鄉">911 竹田鄉</option><option value="內埔鄉">912 內埔鄉</option><option value="萬丹鄉">913 萬丹鄉</option><option value="潮州鎮">920 潮州鎮</option><option value="泰武鄉">921 泰武鄉</option><option value="來義鄉">922 來義鄉</option><option value="萬巒鄉">923 萬巒鄉</option><option value="崁頂鄉">924 崁頂鄉</option><option value="新埤鄉">925 新埤鄉</option><option value="南州鄉">926 南州鄉</option><option value="林邊鄉">927 林邊鄉</option><option value="東港鎮">928 東港鎮</option><option value="琉球鄉">929 琉球鄉</option><option value="佳冬鄉">931 佳冬鄉</option><option value="新園鄉">932 新園鄉</option><option value="枋寮鄉">940 枋寮鄉</option><option value="枋山鄉">941 枋山鄉</option><option value="春日鄉">942 春日鄉</option><option value="獅子鄉">943 獅子鄉</option><option value="車城鄉">944 車城鄉</option><option value="牡丹鄉">945 牡丹鄉</option><option value="恆春鎮">946 恆春鎮</option><option value="滿州鄉">947 滿州鄉</option></select>',
                '<select name="district"><option value="臺東市">950 臺東市</option><option value="綠島鄉">951 綠島鄉</option><option value="蘭嶼鄉">952 蘭嶼鄉</option><option value="延平鄉">953 延平鄉</option><option value="卑南鄉">954 卑南鄉</option><option value="鹿野鄉">955 鹿野鄉</option><option value="關山鎮">956 關山鎮</option><option value="海端鄉">957 海端鄉</option><option value="池上鄉">958 池上鄉</option><option value="東河鄉">959 東河鄉</option><option value="成功鎮">961 成功鎮</option><option value="長濱鄉">962 長濱鄉</option><option value="太麻里鄉">963 太麻里鄉</option><option value="金峰鄉">964 金峰鄉</option><option value="大武鄉">965 大武鄉</option><option value="達仁鄉">966 達仁鄉</option></select>',
                '<select name="district"><option value="花蓮市">970 花蓮市</option><option value="新城鄉">971 新城鄉</option><option value="秀林鄉">972 秀林鄉</option><option value="吉安鄉">973 吉安鄉</option><option value="壽豐鄉">974 壽豐鄉</option><option value="鳳林鎮">975 鳳林鎮</option><option value="光復鄉">976 光復鄉</option><option value="豐濱鄉">977 豐濱鄉</option><option value="瑞穗鄉">978 瑞穗鄉</option><option value="萬榮鄉">979 萬榮鄉</option><option value="玉里鎮">981 玉里鎮</option><option value="卓溪鄉">982 卓溪鄉</option><option value="富里鄉">983 富里鄉</option></select>',
                '<select name="district"><option value="金沙鎮">890 金沙鎮</option><option value="金湖鎮">891 金湖鎮</option><option value="金寧鄉">892 金寧鄉</option><option value="金城鎮">893 金城鎮</option><option value="烈嶼鄉">894 烈嶼鄉</option><option value="烏坵鄉">896 烏坵鄉</option></select>',
                '<select name="district"><option value="南竿鄉">209 南竿鄉</option><option value="北竿鄉">210 北竿鄉</option><option value="莒光鄉">211 莒光鄉</option><option value="東引鄉">212 東引鄉</option></select>',
                '<select name="district"><option value="馬公市">880 馬公市</option><option value="西嶼鄉">881 西嶼鄉</option><option value="望安鄉">882 望安鄉</option><option value="七美鄉">883 七美鄉</option><option value="白沙鄉">884 白沙鄉</option><option value="湖西鄉">885 湖西鄉</option></select>',
            ]

            areas = []
            for i in range(0,len(list_of_county)):
                cty = re.findall('value="(\w+)"',list_of_county[i])
                areas.append(cty)
            
            for i in range(0, len(cities)):
                # print('===============================')
                # print(i)
                # print(cities[i])
                for j in range(0, len(areas[i])):
                    # print(j)
                    # print(areas[i][j])
                    yield scrapy.Request(
                        'https://www.aptg.com.tw/store/stores/district/'+areas[i][j]+'/'+cities[i],
                        self.parse,
                        method='GET'
                    )
                


    def parse(self, response):
        print('===============================')
        json_response = json.loads(response.text)
        # print(json_respone)
        for i in range(len(json_response)):
            item = APTStoreItem()
        #     # print(datas[i]['storeType'])
            item['storeType'] = json_response[i]['tags'][0]
            item['name'] = json_response[i]['name']
            item['address'] = json_response[i]['address']
            item['lonlat'] = json_response[i]['lonlat']
            item['city'] = json_response[i]['city']
            item['county'] = json_response[i]['district']
            yield item
        print('===============================')
