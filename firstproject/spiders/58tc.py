# -*- coding: utf-8 -*-
import scrapy
from firstproject.items import FirstprojectItem

class WbtcSpider(scrapy.Spider):
    name = "58tc"
    start_urls = ['http://bj.58.com/chuzu/pn'+ str(page) + '/?PGTID=0d3090a7-0000-1696-f482-edff6d706232&ClickID=3' for page in range(1, 70)]
    # 定义处理响应函数，函数名必须为parse
    def parse(self, response):
        li_list = response.xpath('//ul[@class="listUl"]/li')
        items = []
        for li in li_list:
            # 房间描述
            item = FirstprojectItem()
            room_des = ''.join( li.xpath('.//div[@class="des"]/h2/a/text()').extract()).strip()
            if room_des:
                item['des'] = room_des
                # 户型和面积
                areas = ''.join( li.xpath('.//div[@class="des"]/p[@class="room"]/text()').extract()).strip().split(' ')
                room_area = areas[0].strip() + areas[-1].strip()
                item['area'] = room_area
                # 地址
                item['address'] = ''
                address_1 = li.xpath('.//div[@class="des"]/p[@class="add"]/a[1]/text()').extract()
                address_2 = li.xpath('.//div[@class="des"]/p[@class="add"]/a[2]/text()').extract()
                address_3 = li.xpath('.//div[@class="des"]/p[@class="add"]/text()').extract()
                # 详细地址描述
                if len(address_1):
                    item['address'] += address_1[0].strip()
                if len(address_2):
                    item['address'] += address_2[0].strip()
                if len(address_3):
                    add = ''
                    for ad in address_3:
                        if ad not in ['\n', '\r',' ', '\t']:
                            add += ad
                        item['address'] += add.strip()
                # 价格
                room_price = ''.join( li.xpath('.//div[@class="money"]//text()').extract() ).strip()
                item['price'] = room_price
            items.append(item)
        return items