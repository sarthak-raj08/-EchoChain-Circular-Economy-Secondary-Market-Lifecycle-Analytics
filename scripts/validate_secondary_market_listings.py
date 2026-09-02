import pandas as pd
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

LISTINGS_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "secondary_market_listings.csv"
)

MAIN_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "EchoChain_Data.csv"
)


# ============================================================
# LOAD DATA
# ============================================================

listings = pd.read_csv(LISTINGS_FILE)
main = pd.read_csv(MAIN_FILE)


print("=" * 60)
print("SECONDARY MARKET LISTINGS VALIDATION")
print("=" * 60)


# ============================================================
# 1. DATASET SHAPE
# ============================================================

print("\n1. DATASET SHAPE")
print("-" * 40)

print("Rows    :", len(listings))
print("Columns :", len(listings.columns))

if len(listings) == 1000:
    print("✅ Row count correct")
else:
    print("❌ Row count incorrect")


# ============================================================
# 2. COLUMN VALIDATION
# ============================================================

expected_columns = [
    "Listing_ID",
    "Product_ID",
    "Product_Category",
    "Product_Name",
    "Brand",
    "Condition",
    "Market_Value_INR",
    "Listing_Price_INR",
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

print("\n2. COLUMN VALIDATION")
print("-" * 40)

missing_columns = set(expected_columns) - set(listings.columns)
extra_columns = set(listings.columns) - set(expected_columns)

if not missing_columns:
    print("✅ All expected columns are present")
else:
    print("❌ Missing columns:", missing_columns)

if not extra_columns:
    print("✅ No extra columns")
else:
    print("❌ Extra columns:", extra_columns)


# ============================================================
# 3. MISSING VALUES
# ============================================================

print("\n3. MISSING VALUES")
print("-" * 40)

missing_values = listings.isnull().sum()

print(missing_values)

if missing_values.sum() == 0:
    print("✅ No missing values")
else:
    print("⚠️ Missing values found")


# ============================================================
# 4. DUPLICATE RECORDS
# ============================================================

print("\n4. DUPLICATE RECORDS")
print("-" * 40)

duplicate_records = listings.duplicated().sum()

print("Duplicate records:", duplicate_records)

if duplicate_records == 0:
    print("✅ No duplicate records")
else:
    print("❌ Duplicate records found")


# ============================================================
# 5. LISTING ID VALIDATION
# ============================================================

print("\n5. LISTING ID VALIDATION")
print("-" * 40)

duplicate_listing_ids = listings["Listing_ID"].duplicated().sum()
empty_listing_ids = listings["Listing_ID"].isna().sum()

print("Duplicate Listing IDs:", duplicate_listing_ids)
print("Empty Listing IDs    :", empty_listing_ids)

if duplicate_listing_ids == 0 and empty_listing_ids == 0:
    print("✅ Listing IDs are unique")
else:
    print("❌ Listing ID validation failed")


# ============================================================
# 6. PRODUCT ID VALIDATION
# ============================================================

print("\n6. PRODUCT ID VALIDATION")
print("-" * 40)

duplicate_product_ids = listings["Product_ID"].duplicated().sum()
empty_product_ids = listings["Product_ID"].isna().sum()

print("Duplicate Product IDs:", duplicate_product_ids)
print("Empty Product IDs    :", empty_product_ids)

if duplicate_product_ids == 0 and empty_product_ids == 0:
    print("✅ Product IDs are unique")
else:
    print("❌ Product ID validation failed")


# ============================================================
# 7. PRODUCT ID REFERENTIAL CHECK
# ============================================================

print("\n7. PRODUCT ID REFERENTIAL CHECK")
print("-" * 40)

invalid_product_ids = (
    ~listings["Product_ID"].isin(main["Product_ID"])
).sum()

print("Product IDs not found in main dataset:", invalid_product_ids)

if invalid_product_ids == 0:
    print("✅ All Product IDs exist in EchoChain_Data.csv")
else:
    print("❌ Invalid Product IDs found")


# ============================================================
# 8. PRICE VALIDATION
# ============================================================

print("\n8. PRICE VALIDATION")
print("-" * 40)

market_value_invalid = (
    listings["Market_Value_INR"].isna().sum()
)

market_value_negative = (
    (listings["Market_Value_INR"] < 0).sum()
)

listing_price_invalid = (
    listings["Listing_Price_INR"].isna().sum()
)

listing_price_negative = (
    (listings["Listing_Price_INR"] < 0).sum()
)

print("Market Value missing :", market_value_invalid)
print("Market Value negative:", market_value_negative)

print("Listing Price missing :", listing_price_invalid)
print("Listing Price negative:", listing_price_negative)

if (
    market_value_invalid == 0
    and market_value_negative == 0
    and listing_price_invalid == 0
    and listing_price_negative == 0
):
    print("✅ Price validation passed")
else:
    print("❌ Price validation failed")


# ============================================================
# 9. CUSTOMER RATING VALIDATION
# ============================================================

print("\n9. CUSTOMER RATING VALIDATION")
print("-" * 40)

invalid_ratings = (
    (listings["Customer_Rating"] < 0)
    | (listings["Customer_Rating"] > 5)
).sum()

print("Invalid ratings:", invalid_ratings)

if invalid_ratings == 0:
    print("✅ Rating validation passed")
else:
    print("❌ Rating validation failed")


# ============================================================
# 10. PRODUCT CATEGORY
# ============================================================

print("\n10. PRODUCT CATEGORY")
print("-" * 40)

print(listings["Product_Category"].value_counts())

# ============================================================
# 11. PLATFORM
# ============================================================

print("\n11. PLATFORM")
print("-" * 40)

print(listings["Platform"].value_counts())


# ============================================================
# 12. CONDITION
# ============================================================

print("\n12. CONDITION")
print("-" * 40)

print(listings["Condition"].value_counts())


# ============================================================
# 13. FINAL DISPOSITION
# ============================================================

print("\n13. FINAL DISPOSITION")
print("-" * 40)

print(listings["Final_Disposition"].value_counts())


# ============================================================
# FINAL RESULT
# ============================================================

print("\n" + "=" * 60)
print("FINAL VALIDATION RESULT")
print("=" * 60)

critical_checks = [
    len(listings) == 1000,
    not missing_columns,
    not extra_columns,
    missing_values.sum() == 0,
    duplicate_records == 0,
    duplicate_listing_ids == 0,
    empty_listing_ids == 0,
    duplicate_product_ids == 0,
    empty_product_ids == 0,
    invalid_product_ids == 0,
    market_value_invalid == 0,
    market_value_negative == 0,
    listing_price_invalid == 0,
    listing_price_negative == 0,
    invalid_ratings == 0
]

if all(critical_checks):
    print("STATUS: PASSED ✅")
    print("Secondary market listings dataset is valid.")
else:
    print("STATUS: FAILED ❌")
    print("Please fix the validation issues.")

print("=" * 60)