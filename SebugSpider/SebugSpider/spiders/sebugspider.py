#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from SebugSpider.items import VulnItem


class SebugSpider(CrawlSpider):
    name = 'sebug'
    allowed_domains = ['sebug.net']
    start_urls = ['http://sebug.net/vuldb/vulnerabilities?start=1']

    rules = [
        # scrapy the page links and take the default parse to process it
        Rule(LinkExtractor(allow=['/vuldb/vulnerabilities\?start=\d+']), ),

        # scrapy every vuln link and extract VulnItem
        Rule(LinkExtractor(allow=['/vuldb/ssvid-\d+']), callback='parse_vuln')
    ]

    def parse_vuln(self, response):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')

        vuln = VulnItem()
        content = response.xpath('//div[@id="main"]/div[@id="content"]')
        vuln['ssvid'] = re.findall('\d+', response.url)[0]
        vuln['date'] = re.findall('\d+-\d+-\d+', content.xpath('//div[@class="at_sebug"]/text()').extract()[0])[0]
        vuln['title'] = content.xpath('//h2[@class="article_title"]/text()').extract()[0]
        vuln['content'] = content.extract()[0]

        return vuln
