import pandas as pd
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "EchoChain_Data.csv"

OUTPUT_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "secondary_market_listings.csv"
)


# ============================================================
# READ MAIN DATA
# ============================================================

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("CREATING SECONDARY MARKET LISTINGS")
print("=" * 60)

print(f"\nOriginal dataset shape: {df.shape}")


# ============================================================
# SELECT 1000 RECORDS
# ============================================================

listings = df.head(1000).copy()


# ============================================================
# CREATE LISTING ID
# ============================================================

listings.insert(
    0,
    "Listing_ID",
    [f"LISTING_{i:05d}" for i in range(1, len(listings) + 1)]
)


# ============================================================
# SELECT MARKETPLACE-RELEVANT COLUMNS
# ============================================================

listings = listings[
    [
        "Listing_ID",
        "Product_ID",
        "Product_Category",
        "Product_Name",
        "Brand",
        "Condition_at_Resale",
        "Current_Market_Value_INR",
        "Resale_Price_INR",
        "Seller_Type",
        "Buyer_Type",
        "Platform",
        "Refurbished",
        "Refurbishment_Cost_INR",
        "Repair_Count",
        "Product_Age_Months",
        "Usage_Hours",
        "Warranty_Status",
        "Return_Status",
        "Region",
        "City",
        "Customer_Rating",
        "Final_Disposition"
    ]
]


# ============================================================
# RENAME COLUMNS FOR LISTING DATA
# ============================================================

listings = listings.rename(
    columns={
        "Condition_at_Resale": "Condition",
        "Current_Market_Value_INR": "Market_Value_INR",
        "Resale_Price_INR": "Listing_Price_INR"
    }
)


# ============================================================
# SAVE FILE
# ============================================================

listings.to_csv(
    OUTPUT_FILE,
    index=False
)


# ============================================================
# FINAL INFORMATION
# ============================================================

print("\nListing dataset created successfully!")

print(f"Final Shape: {listings.shape}")

print("\nColumns:")
for column in listings.columns:
    print(column)

print("\nOutput File:")
print(OUTPUT_FILE)

print("\nFirst 5 records:")
print(listings.head())

print("\n" + "=" * 60)
print("PROCESS COMPLETED")
print("=" * 60)