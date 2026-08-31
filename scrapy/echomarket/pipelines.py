class EchomarketPipeline:

    def process_item(self, item, spider):

        # Remove extra spaces from text fields
        for field in ["Product_Name", "Price", "Availability", "Rating"]:
            if field in item and item[field]:
                item[field] = item[field].strip()

        # Clean Price
        if item.get("Price"):
            item["Price"] = (
                item["Price"]
                .replace("£", "")
                .strip()
            )

        # Clean Rating
        if item.get("Rating"):
            rating_class = item["Rating"].split()

            if len(rating_class) > 1:
                item["Rating"] = rating_class[-1]

        return item