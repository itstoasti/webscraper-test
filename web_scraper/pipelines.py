```python
import json
from scrapy.exceptions import DropItem
from .items import RedditItem

class RedditScraperPipeline:
    def open_spider(self, spider):
        self.file = open('output.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, RedditItem):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Unknown item found: %s" % item)
```