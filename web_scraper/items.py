```python
import scrapy

class RedditItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    upvotes = scrapy.Field()
    comments = scrapy.Field()
```