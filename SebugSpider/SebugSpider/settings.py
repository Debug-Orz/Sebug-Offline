# -*- coding: utf-8 -*-

# Scrapy settings for SebugSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'SebugSpider'

SPIDER_MODULES = ['SebugSpider.spiders']
NEWSPIDER_MODULE = 'SebugSpider.spiders'

ITEM_PIPELINES = {
    'SebugSpider.pipelines.SebugPipeline'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SebugSpider (+http://www.yourdomain.com)'
