# -*- coding: utf-8 -*-

# Scrapy settings for sebugspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sebugspider'

SPIDER_MODULES = ['sebugspider.spiders']
NEWSPIDER_MODULE = 'sebugspider.spiders'

ITEM_PIPELINES = {
    'sebugspider.pipelines.SebugspiderPipeline'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sebugspider (+http://www.yourdomain.com)'
