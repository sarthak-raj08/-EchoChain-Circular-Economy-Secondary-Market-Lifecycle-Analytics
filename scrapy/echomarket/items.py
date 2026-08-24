import scrapy


class MarketplaceItem(scrapy.Item):
    listing_id = scrapy.Field()
    product_name = scrapy.Field()
    brand = scrapy.Field()
    product_category = scrapy.Field()
    price_inr = scrapy.Field()
    condition = scrapy.Field()
    seller_type = scrapy.Field()
    city = scrapy.Field()
    platform = scrapy.Field()
    listing_date = scrapy.Field()
    refurbished = scrapy.Field()
    warranty_status = scrapy.Field()
    availability = scrapy.Field()