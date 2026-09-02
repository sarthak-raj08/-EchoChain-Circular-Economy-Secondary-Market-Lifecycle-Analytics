import pandas as pd
from pathlib import Path


# ============================================================
# MARKETPLACE ANALYSIS
# ============================================================

print("=" * 60)
print("MARKETPLACE DATA ANALYSIS")
print("=" * 60)


# ------------------------------------------------------------
# 1. FILE PATHS
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "marketplace_analytics.csv"
)

OUTPUT_DIR = (
    BASE_DIR
    / "data"
    / "processed"
)


# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------

print("\n1. LOADING DATA")
print("-" * 40)

df = pd.read_csv(INPUT_FILE)

print(f"Dataset Shape: {df.shape}")
print(f"Rows         : {len(df)}")
print(f"Columns      : {len(df.columns)}")


# ------------------------------------------------------------
# 3. BASIC INFORMATION
# ------------------------------------------------------------

print("\n2. BASIC DATA INFORMATION")
print("-" * 40)

print("\nProduct Categories:")
print(df["Product_Category"].value_counts())

print("\nPlatforms:")
print(df["Platform"].value_counts())

print("\nConditions:")
print(df["Condition"].value_counts())

print("\nPricing Categories:")
print(df["Pricing_Category"].value_counts())


# ------------------------------------------------------------
# 4. PRICE ANALYSIS
# ------------------------------------------------------------

print("\n3. PRICE ANALYSIS")
print("-" * 40)

print(
    f"Average Market Value   : "
    f"{df['Market_Value_INR'].mean():,.2f}"
)

print(
    f"Average Listing Price  : "
    f"{df['Listing_Price_INR'].mean():,.2f}"
)

print(
    f"Minimum Market Value   : "
    f"{df['Market_Value_INR'].min():,.2f}"
)

print(
    f"Maximum Market Value   : "
    f"{df['Market_Value_INR'].max():,.2f}"
)

print(
    f"Minimum Listing Price  : "
    f"{df['Listing_Price_INR'].min():,.2f}"
)

print(
    f"Maximum Listing Price  : "
    f"{df['Listing_Price_INR'].max():,.2f}"
)


# ------------------------------------------------------------
# 5. DISCOUNT ANALYSIS
# ------------------------------------------------------------

print("\n4. DISCOUNT ANALYSIS")
print("-" * 40)

print(
    f"Average Discount       : "
    f"{df['Discount_Percentage'].mean():.2f}%"
)

print(
    f"Minimum Discount       : "
    f"{df['Discount_Percentage'].min():.2f}%"
)

print(
    f"Maximum Discount       : "
    f"{df['Discount_Percentage'].max():.2f}%"
)

print(
    f"Median Discount        : "
    f"{df['Discount_Percentage'].median():.2f}%"
)


# ------------------------------------------------------------
# 6. MARKET VALUE VS LISTING PRICE
# ------------------------------------------------------------

print("\n5. MARKET VALUE VS LISTING PRICE")
print("-" * 40)

below_market = (
    df["Pricing_Category"]
    .eq("Below Market Value")
    .sum()
)

above_market = (
    df["Pricing_Category"]
    .eq("Above Market Value")
    .sum()
)

print(f"Below Market Value     : {below_market}")
print(f"Above Market Value     : {above_market}")

print(
    f"Below Market %         : "
    f"{below_market / len(df) * 100:.2f}%"
)

print(
    f"Above Market %         : "
    f"{above_market / len(df) * 100:.2f}%"
)


# ------------------------------------------------------------
# 7. PLATFORM ANALYSIS
# ------------------------------------------------------------

print("\n6. PLATFORM ANALYSIS")
print("-" * 40)

platform_summary = (
    df.groupby("Platform")
    .agg(
        Listings=("Listing_ID", "count"),
        Avg_Market_Value=("Market_Value_INR", "mean"),
        Avg_Listing_Price=("Listing_Price_INR", "mean"),
        Avg_Discount=("Discount_Percentage", "mean"),
    )
    .sort_values(
        "Listings",
        ascending=False
    )
)

print(platform_summary.round(2))


# ------------------------------------------------------------
# 8. PRODUCT CATEGORY ANALYSIS
# ------------------------------------------------------------

print("\n7. PRODUCT CATEGORY ANALYSIS")
print("-" * 40)

category_summary = (
    df.groupby("Product_Category")
    .agg(
        Listings=("Listing_ID", "count"),
        Avg_Market_Value=("Market_Value_INR", "mean"),
        Avg_Listing_Price=("Listing_Price_INR", "mean"),
        Avg_Discount=("Discount_Percentage", "mean"),
    )
    .sort_values(
        "Listings",
        ascending=False
    )
)

print(category_summary.round(2))


# ------------------------------------------------------------
# 9. CONDITION ANALYSIS
# ------------------------------------------------------------

print("\n8. CONDITION ANALYSIS")
print("-" * 40)

condition_summary = (
    df.groupby("Condition")
    .agg(
        Listings=("Listing_ID", "count"),
        Avg_Market_Value=("Market_Value_INR", "mean"),
        Avg_Listing_Price=("Listing_Price_INR", "mean"),
        Avg_Discount=("Discount_Percentage", "mean"),
        Avg_Rating=("Customer_Rating", "mean"),
    )
    .sort_values(
        "Listings",
        ascending=False
    )
)

print(condition_summary.round(2))


# ------------------------------------------------------------
# 10. CUSTOMER RATING ANALYSIS
# ------------------------------------------------------------

print("\n9. CUSTOMER RATING ANALYSIS")
print("-" * 40)

print(
    f"Average Customer Rating : "
    f"{df['Customer_Rating'].mean():.2f}"
)

print(
    f"Highest Customer Rating  : "
    f"{df['Customer_Rating'].max():.2f}"
)

print(
    f"Lowest Customer Rating   : "
    f"{df['Customer_Rating'].min():.2f}"
)


# ------------------------------------------------------------
# 11. REFURBISHMENT ANALYSIS
# ------------------------------------------------------------

print("\n10. REFURBISHMENT ANALYSIS")
print("-" * 40)

print(
    df["Refurbished"]
    .value_counts()
)

refurbished_count = (
    df["Refurbished"]
    .astype(str)
    .str.lower()
    .eq("yes")
    .sum()
)

print(
    f"\nRefurbished Listings : "
    f"{refurbished_count}"
)

print(
    f"Refurbished %        : "
    f"{refurbished_count / len(df) * 100:.2f}%"
)


# ------------------------------------------------------------
# 12. FINAL DISPOSITION ANALYSIS
# ------------------------------------------------------------

print("\n11. FINAL DISPOSITION ANALYSIS")
print("-" * 40)

print(
    df["Final_Disposition"]
    .value_counts()
)


# ------------------------------------------------------------
# 13. REGIONAL ANALYSIS
# ------------------------------------------------------------

print("\n12. REGIONAL ANALYSIS")
print("-" * 40)

region_summary = (
    df.groupby("Region")
    .agg(
        Listings=("Listing_ID", "count"),
        Avg_Market_Value=("Market_Value_INR", "mean"),
        Avg_Listing_Price=("Listing_Price_INR", "mean"),
        Avg_Discount=("Discount_Percentage", "mean"),
        Avg_Rating=("Customer_Rating", "mean"),
    )
    .sort_values(
        "Listings",
        ascending=False
    )
)

print(region_summary.round(2))


# ------------------------------------------------------------
# 14. TOP DISCOUNTED PRODUCTS
# ------------------------------------------------------------

print("\n13. TOP 10 DISCOUNTED PRODUCTS")
print("-" * 40)

top_discounted = (
    df[
        [
            "Product_Name",
            "Product_Category",
            "Platform",
            "Market_Value_INR",
            "Listing_Price_INR",
            "Discount_Percentage",
        ]
    ]
    .sort_values(
        "Discount_Percentage",
        ascending=False
    )
    .head(10)
)

print(top_discounted.to_string(index=False))


# ------------------------------------------------------------
# 15. TOP MARKET VALUE PRODUCTS
# ------------------------------------------------------------

print("\n14. TOP 10 PRODUCTS BY MARKET VALUE")
print("-" * 40)

top_market_value = (
    df[
        [
            "Product_Name",
            "Product_Category",
            "Platform",
            "Market_Value_INR",
            "Listing_Price_INR",
            "Customer_Rating",
        ]
    ]
    .sort_values(
        "Market_Value_INR",
        ascending=False
    )
    .head(10)
)

print(top_market_value.to_string(index=False))


# ------------------------------------------------------------
# 16. SAVE SUMMARY FILES
# ------------------------------------------------------------

print("\n15. SAVING ANALYSIS RESULTS")
print("-" * 40)

platform_output = OUTPUT_DIR / "platform_analysis.csv"
category_output = OUTPUT_DIR / "category_analysis.csv"
condition_output = OUTPUT_DIR / "condition_analysis.csv"
region_output = OUTPUT_DIR / "region_analysis.csv"
top_discount_output = OUTPUT_DIR / "top_discounted_products.csv"

platform_summary.round(2).to_csv(
    platform_output
)

category_summary.round(2).to_csv(
    category_output
)

condition_summary.round(2).to_csv(
    condition_output
)

region_summary.round(2).to_csv(
    region_output
)

top_discounted.to_csv(
    top_discount_output,
    index=False
)


# ------------------------------------------------------------
# 17. FINAL RESULT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MARKETPLACE ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nAnalysis files created:")

print(f"1. {platform_output}")
print(f"2. {category_output}")
print(f"3. {condition_output}")
print(f"4. {region_output}")
print(f"5. {top_discount_output}")

print("\n" + "=" * 60)