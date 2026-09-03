import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def test_marketplace_analytics_shape():
    file = BASE_DIR / "data" / "processed" / "marketplace_analytics.csv"
    df = pd.read_csv(file)

    assert len(df) == 1000
    assert len(df.columns) == 41


def test_price_difference_calculation():
    file = BASE_DIR / "data" / "processed" / "marketplace_analytics.csv"
    df = pd.read_csv(file)

    expected = (
        df["Market_Value_INR"] - df["Listing_Price_INR"]
    ).round(2)

    assert (df["Price_Difference_INR"] - expected).abs().max() < 0.01


def test_discount_percentage_calculation():
    file = BASE_DIR / "data" / "processed" / "marketplace_analytics.csv"
    df = pd.read_csv(file)

    expected = (
        (df["Market_Value_INR"] - df["Listing_Price_INR"])
        / df["Market_Value_INR"]
        * 100
    ).round(2)

    assert (df["Discount_Percentage"] - expected).abs().max() < 0.01


def test_listing_to_market_ratio():
    file = BASE_DIR / "data" / "processed" / "marketplace_analytics.csv"
    df = pd.read_csv(file)

    expected = (
        df["Listing_Price_INR"] / df["Market_Value_INR"]
    ).round(2)

    assert (df["Listing_to_Market_Ratio"] - expected).abs().max() < 0.01


def test_pricing_categories_are_valid():
    file = BASE_DIR / "data" / "processed" / "marketplace_analytics.csv"
    df = pd.read_csv(file)

    valid_categories = {
        "Below Market Value",
        "Above Market Value",
        "At Market Value",
    }

    assert set(df["Pricing_Category"]).issubset(valid_categories)
