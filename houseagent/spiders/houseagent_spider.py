from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy import log
from houseagent.items import HouseagentItem

class HouseagentSpider(CrawlSpider):
    
    name = "Houseagent"

    allowed_domains = ["http://hz.5i5j.com"]
    start_urls = ['http://hz.5i5j.com/broker/n%d/' %n for n in range (1,2)]
    #allowed_domains = ["http://esf.hz.soufun.com"]
    #start_urls = ['http://esf.hz.soufun.com/agenthome/-i3%d-j310/' %n for n in range (1,2)]
    rules = ()
    def parse(self,response):
        print "Start scrapping House Agent papers info..."
        hxs=HtmlXPathSelector(response)
        bases = hxs.select('/html/body/div/div/div/div/*')
        items=[]
        for base in bases:
            item = HouseagentItem()
            item['telephone'] = base.select('div/div/span/span/a//text()').split(',')
            items.append(item)
        return(items)