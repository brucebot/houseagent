from scrapy.exceptions import DropItem

class HouseagentPipeline(object):
    def process_item(self, item, spider):
        if not(item["telephone"]):
            raise DropItem()
        else:
            return item
            
class DropIfEmptyFieldPipeline(object):
    def process_item(self,item,spider):
        if not(all(item.values())):
            raise DropItem()
        else:
            return item