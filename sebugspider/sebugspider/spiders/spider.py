#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'rickgray'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from sebugspider.items import VulnItem
import re, cgi, HTMLParser


class SebugSpider(CrawlSpider):
    """
    'sebug' spider, which extract vuln info from [sebug.net]

    """
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
        vuln = VulnItem()

        content = response.xpath('//div[@id="main"]/div[@id="content"]')
        vuln['ssvid'] = re.findall('\d+', response.url)[0]

        pre_date = content.xpath('//div[@class="vuln"]/text()').extract()
        for pre_content in pre_date:
            if re.search('(\d+-\d+-\d+)', pre_content):
                vuln['date'] = re.findall('(\d+-\d+-\d+)', pre_content)[0]
        # vuln['date'] = re.findall('\d+-\d+-\d+', content.xpath('//div[@class="at_sebug"]/text()').extract()[0])[0]

        html_parser = HTMLParser.HTMLParser()
        vuln['title'] = cgi.escape(html_parser.unescape(
            re.findall('<h2 class="article_title">(.*)</h2>', response.body_as_unicode())[0]))
        # vuln['title'] = content.xpath('//h2[@class="article_title"]/text()').extract()[0]
        vuln['content'] = content.extract()[0]

        # handle the content special encode
        vuln['content'] = vuln['content'].replace('*&gt;','')

        return vuln
