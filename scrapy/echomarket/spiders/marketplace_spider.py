# import scrapy


# class MarketplaceSpider(scrapy.Spider):

#     name = "marketplace"

#     start_urls = [
#         "TARGET_WEBSITE_URL"
#     ]

#     def parse(self, response):

#         for product in response.css("PRODUCT_SELECTOR"):

#             yield {
#                 "Product_Name": product.css("NAME_SELECTOR::text").get(),
#                 "Brand": product.css("BRAND_SELECTOR::text").get(),
#                 "Price_INR": product.css("PRICE_SELECTOR::text").get(),
#                 "Condition": product.css("CONDITION_SELECTOR::text").get(),
#                 "Location": product.css("LOCATION_SELECTOR::text").get(),
#             }

import scrapy


class MarketplaceSpider(scrapy.Spider):

    name = "marketplace"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        for book in response.css("article.product_pod"):

            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
                "availability": book.css("p.instock.availability::text").getall(),
                "product_url": book.css("h3 a::attr(href)").get(),
            }

