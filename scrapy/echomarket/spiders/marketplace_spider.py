import scrapy


class MarketplaceSpider(scrapy.Spider):

    name = "marketplace"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        products = response.css("article.product_pod")

        self.logger.info(
            f"Products found: {len(products)}"
        )

        for product in products:

            yield {
                "Product_Name": product.css(
                    "h3 a::attr(title)"
                ).get(),

                "Price": product.css(
                    ".price_color::text"
                ).get(),

                "Availability": product.css(
                    ".availability::text"
                ).getall(),

                "Rating": product.css(
                    "p.star-rating::attr(class)"
                ).get(),

                "Product_URL": product.css(
                    "h3 a::attr(href)"
                ).get(),

                "Image_URL": product.css(
                    "img::attr(src)"
                ).get()
            }