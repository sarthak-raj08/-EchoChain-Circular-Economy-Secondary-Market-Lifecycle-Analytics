import scrapy


class MarketplaceListingItem(scrapy.Item):
    listing_id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    condition = scrapy.Field()
    seller = scrapy.Field()
    listing_date = scrapy.Field()