import scrapy


class EchomarketItem(scrapy.Item):
    product_name = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    condition = scrapy.Field()
    seller_type = scrapy.Field()
    location = scrapy.Field()
    product_url = scrapy.Field()
    scraped_date = scrapy.Field()