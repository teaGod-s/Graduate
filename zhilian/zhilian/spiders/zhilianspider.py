# -*- coding: utf-8 -*-
import scrapy
from zhilian.items import ZhilianItem


class ZhilianspiderSpider(scrapy.Spider):
    name = 'zhilianspider'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/']

    def start_requests(self):
        urls = [
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=上海&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=北京&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=广州&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=杭州&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=武汉&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=天津&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=成都&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=西安&p=1&isadv=0",
            "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=大连&p=1&isadv=0"
        ]
        for url in urls:
            yield scrapy.Request(url, self.parse)
        # url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=上海&p=1&isadv=0"
        # yield scrapy.Request(url, self.parse)

    def parse(self, response):
        table_list = response.xpath('//table[@class="newlist"]')
        # print(table_list)
        for table in table_list[2:]:
            item = ZhilianItem()
            position = table.xpath('.//td[@class="zwmc"]/div/a[1]/text()').extract_first()
            item["position"] = position.strip() if position else None

            url = table.xpath('.//td[@class="zwmc"]/div/a[1]/@href').extract_first()
            item["link"] = url.strip() if url else None
            if url:
                yield scrapy.Request(url=url, meta={"item": item}, callback=self.parse_link, dont_filter=True)
        next_page = response.xpath('//li[@class="pagesDown-pos"]/a/@href').extract_first()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse_link(self, response):
        item = response.meta['item']
        company = response.xpath('//div[@class="fixed-inner-box"]//h2/a/text()').extract_first()
        item["company"] = company.strip() if company else None

        salary = response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first()
        item["salary"] = salary.strip() if salary else None

        workplace = response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()').extract_first()
        item["workplace"] = workplace.strip() if workplace else None

        education = response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract_first()
        item["education"] = education.strip() if education else None

        experience = response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()').extract_first()
        item["experience"] = experience.strip() if experience else None

        size = response.xpath(
            '//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[1]/strong/text()').extract_first()
        item["size"] = size.strip() if size else None

        attribute = response.xpath(
            '//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[2]/strong/text()').extract_first()
        item["attribute"] = attribute.strip() if attribute else None

        field = response.xpath(
            '//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[3]//a/text()').extract_first()
        item["field"] = field.strip() if field else None

        inner_cont = response.xpath('//div[@class="terminalpage-main clearfix"]/div[1]/div[1]')
        description = ''
        if len(inner_cont.xpath('./p[1]/span[2]')) > 0:
            desc_str_list = inner_cont.xpath('./p[1]/span[2]/text()').extract()
            for desc_str in desc_str_list:
                description += desc_str.strip()
            item["description"] = description.strip() if description else None
        else:
            desc_str_list = inner_cont.xpath('./p/text()').extract()
            for desc_str in desc_str_list:
                description += desc_str.strip()
            item["description"] = description.strip() if description else None
        yield item
