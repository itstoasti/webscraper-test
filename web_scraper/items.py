```python
import scrapy

class GoogleItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    snippet = scrapy.Field()
```