from itemloaders import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst


def clean_price(value):
    return value.replace("£", "").strip()


def clean_text(value):
    return value.strip()


def clean_rating(value):
    return value.replace("star-rating", "").strip()


class EchomarketItemLoader(ItemLoader):

    default_output_processor = TakeFirst()

    Product_Name_in = MapCompose(clean_text)
    Price_in = MapCompose(clean_price)
    Availability_in = MapCompose(clean_text)
    Rating_in = MapCompose(clean_rating)
    Product_URL_in = MapCompose(clean_text)
    Image_URL_in = MapCompose(clean_text)