# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class FirstprojectPipeline(object):
    def process_item(self, item, spider):
        with open('58tc.json', 'a+', encoding='utf-8') as fp:
            line = json.dumps(dict(item),ensure_ascii=False)
            fp.write(line)
        return item
