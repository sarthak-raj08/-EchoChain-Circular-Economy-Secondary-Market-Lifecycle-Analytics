import csv
import os


class MarketplaceCsvPipeline:

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def open_spider(self, spider):

        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..")
        )

        output_directory = os.path.join(
            project_root,
            "data",
            "raw",
            "secondary_market"
        )

        os.makedirs(output_directory, exist_ok=True)

        self.file_path = os.path.join(
            output_directory,
            "marketplace_listings.csv"
        )

        self.file = open(
            self.file_path,
            "w",
            newline="",
            encoding="utf-8"
        )

        self.writer = csv.DictWriter(
            self.file,
            fieldnames=[
                "listing_id",
                "title",
                "price",
                "condition",
                "seller",
                "listing_date"
            ]
        )

        self.writer.writeheader()

        spider.logger.info(
            "Output file: %s",
            self.file_path
        )

    def process_item(self, item, spider):

        self.writer.writerow(dict(item))

        return item

    def close_spider(self, spider):

        self.file.close()