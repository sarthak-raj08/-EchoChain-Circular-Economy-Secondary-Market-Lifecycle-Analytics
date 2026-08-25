import scrapy
import csv
import os

from echomarket.items import MarketplaceListingItem


class MarketplaceSpider(scrapy.Spider):
    name = "marketplace"

    def start_requests(self):
        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )

        csv_path = os.path.join(
            project_root,
            "datasets",
            "secondary_market_listings.csv"
        )

        self.logger.info("CSV PATH: %s", csv_path)

        if not os.path.exists(csv_path):
            self.logger.error("CSV FILE NOT FOUND!")
            return

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                yield scrapy.Request(
                    url="https://example.com",
                    callback=self.parse_listing,
                    meta={"listing": row},
                    dont_filter=True
                )

    def parse_listing(self, response):
        row = response.meta["listing"]

        item = MarketplaceListingItem()

        item["listing_id"] = row["listing_id"]
        item["title"] = row["title"]
        item["price"] = float(row["price"])
        item["condition"] = row["condition"]
        item["seller"] = row["seller"]
        item["listing_date"] = row["listing_date"]

        yield item