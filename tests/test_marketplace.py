import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def test_secondary_market_listings():
    file = BASE_DIR / "data" / "raw" / "secondary_market_listings.csv"
    df = pd.read_csv(file)

    assert len(df) == 1000
    assert len(df.columns) == 22


def test_listing_ids_are_unique():
    file = BASE_DIR / "data" / "raw" / "secondary_market_listings.csv"
    df = pd.read_csv(file)

    assert df["Listing_ID"].notna().all()
    assert df["Listing_ID"].is_unique


def test_marketplace_product_ids_are_valid():
    listings = pd.read_csv(
        BASE_DIR / "data" / "raw" / "secondary_market_listings.csv"
    )

    main = pd.read_csv(
        BASE_DIR / "data" / "raw" / "EchoChain_Data.csv"
    )

    assert listings["Product_ID"].isin(main["Product_ID"]).all()


def test_market_values_are_positive():
    file = BASE_DIR / "data" / "raw" / "secondary_market_listings.csv"
    df = pd.read_csv(file)

    assert (df["Market_Value_INR"] > 0).all()
    assert (df["Listing_Price_INR"] > 0).all()


def test_scraped_marketplace_cleaned():
    file = BASE_DIR / "data" / "processed" / "marketplace_cleaned.csv"
    df = pd.read_csv(file)

    assert len(df) == 1000
    assert df["Product_Name"].notna().all()
    assert (df["Price"] > 0).all()
