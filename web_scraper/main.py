```python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from web_scraper.spiders.google_spider import GoogleSpider

def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(GoogleSpider)
    process.start()

if __name__ == "__main__":
    main()
```