import scrapy
from echomarket.items import EchomarketItem
from echomarket.itemloaders import EchomarketItemLoader

class MarketplaceSpider(scrapy.Spider):

    name = "marketplace"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        products = response.css("article.product_pod")

        self.logger.info(
            f"Products found on page: {len(products)}"
        )

        for product in products:

            loader = EchomarketItemLoader(
                item=EchomarketItem(),
                selector=product
            )

            loader.add_css(
                "Product_Name",
                "h3 a::attr(title)"
            )

            loader.add_css(
                "Price",
                ".price_color::text"
            )

            loader.add_css(
                "Availability",
                ".availability::text"
            )

            loader.add_css(
                "Rating",
                "p.star-rating::attr(class)"
            )

            loader.add_css(
                "Product_URL",
                "h3 a::attr(href)"
            )

            loader.add_css(
                "Image_URL",
                "img::attr(src)"
            )

            item = loader.load_item()

            item["Product_URL"] = response.urljoin(
                item["Product_URL"]
            )

            item["Image_URL"] = response.urljoin(
                item["Image_URL"]
            )

            yield item

        next_page = response.css(
            "li.next a::attr(href)"
        ).get()

        if next_page:

            self.logger.info(
                f"Going to next page: {next_page}"
            )

            yield response.follow(
                next_page,
                callback=self.parse
            )