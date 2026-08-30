import scrapy


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

        # Extract product data
        for product in products:

            yield {
                "Product_Name": product.css(
                    "h3 a::attr(title)"
                ).get(),

                "Price": product.css(
                    ".price_color::text"
                ).get(),

                "Availability": " ".join(
                    product.css(
                        ".availability::text"
                    ).getall()
                ).strip(),

                "Rating": product.css(
                    "p.star-rating::attr(class)"
                ).get(),

                "Product_URL": response.urljoin(
                    product.css(
                        "h3 a::attr(href)"
                    ).get()
                ),

                "Image_URL": response.urljoin(
                    product.css(
                        "img::attr(src)"
                    ).get()
                )
            }

        # Find next page
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