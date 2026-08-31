import scrapy


class EchomarketItem(scrapy.Item):

    Product_Name = scrapy.Field()
    Price = scrapy.Field()
    Availability = scrapy.Field()
    Rating = scrapy.Field()
    Product_URL = scrapy.Field()
    Image_URL = scrapy.Field()