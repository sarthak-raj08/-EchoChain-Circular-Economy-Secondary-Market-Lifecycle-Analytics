import scrapy


class MarketplaceSpider(scrapy.Spider):
    name = "marketplace"

    start_urls = [
        "https://example.com"
    ]

    def parse(self, response):
        self.logger.info("Spider is working!")