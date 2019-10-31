# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem


class MoiveSpider(scrapy.Spider):
    name = 'moive'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DoubanmovieItem()
        all_movie_list = response.xpath('//div[@class="item"]')
        for evevry_moive_info in all_movie_list:
            item["count"] = evevry_moive_info.xpath('div[1]/em/text()').extract()
            item["name"] = evevry_moive_info.xpath('div[2]/div[1]/a[1]/span[1]/text()').extract()
            item["director"] = evevry_moive_info.xpath('div[2]//div[2]/p/text()').extract()[0].split('\xa0\xa0\xa0')[0].strip().replace('导演: ','')
            try:
                item["stra"] = evevry_moive_info.xpath('div[2]//div[2]/p/text()').extract()[0].split('\xa0\xa0\xa0')[1].strip().replace('主演: ','').replace('...','')
            except:
                item["stra"] = '空数据'
            item["quote"] = evevry_moive_info.xpath('div[2]//div[2]/p[2]/span/text()').extract()
            yield item
            nextPage = response.xpath('//span[@class="next"]/a/@href')
            # 判断nextPage是否有效
            if nextPage:
                # 拼接下一页的地址
                url = response.urljoin(nextPage[0].extract())
                # 发送url后页请求
                yield scrapy.Request(url, self.parse)
