```python
import scrapy
from web_scraper.items import GoogleItem

class GoogleSpider(scrapy.Spider):
    name = "GoogleSpider"
    allowed_domains = ["www.google.com"]
    start_urls = ["http://www.google.com/"]

    def parse(self, response):
        for result in response.css('div.g'):
            item = GoogleItem()
            item['title'] = result.css('h3.r a::text').get()
            item['link'] = result.css('h3.r a::attr(href)').get()
            item['description'] = result.css('span.st::text').get()
            yield item

        next_page = response.css('a.fl::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```