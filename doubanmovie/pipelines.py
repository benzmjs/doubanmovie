# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


class DoubanmoviePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['数量', '电影名字', '导演', '主演', '概要文字'])

    def process_item(self, item, spider):
        line = [item["count"][0], item["name"][0], item["director"], item["stra"],
                item["quote"][0]]
        self.ws.append(line)
        print(item["count"][0], item["name"][0], item["director"], item["stra"],
                item["quote"][0])
        self.wb.save('douban.xlsx')
        return item
