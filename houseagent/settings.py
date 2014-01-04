# Scrapy settings for houseagent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'houseagent'

SPIDER_MODULES = ['houseagent.spiders']
NEWSPIDER_MODULE = 'houseagent.spiders'
ITEM_PIPELINES=['houseagent.pipelines.DropIfEmptyFieldPipeline',]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'houseagent (+http://www.yourdomain.com)'
