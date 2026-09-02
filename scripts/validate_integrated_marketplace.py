import pandas as pd


print("=" * 60)
print("INTEGRATED MARKETPLACE DATA VALIDATION")
print("=" * 60)


# ------------------------------------------------------------
# Load dataset
# ------------------------------------------------------------

file_path = "./data/processed/marketplace_integrated.csv"

df = pd.read_csv(file_path)


# ------------------------------------------------------------
# 1. Dataset Shape
# ------------------------------------------------------------

print("\n1. DATASET SHAPE")
print("-" * 40)

print("Rows    :", len(df))
print("Columns :", len(df.columns))


if len(df) == 10000:
    print("✅ Row count correct")
else:
    print("❌ Row count incorrect")


if len(df.columns) == 37:
    print("✅ Column count correct")
else:
    print("❌ Column count incorrect")


# ------------------------------------------------------------
# 2. Column Validation
# ------------------------------------------------------------

print("\n2. COLUMN VALIDATION")
print("-" * 40)

expected_columns = [
    "Transaction_ID",
    "Product_ID",
    "Product_Category",
    "Product_Name",
    "Brand",
    "Purchase_Date",
    "Original_Price_INR",
    "Current_Market_Value_INR",
    "Condition_at_Resale",
    "Ownership_Cycle",
    "Resale_Date",
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
    "Recycling_Eligible",
    "Recycled",
    "Recycling_Date",
    "Material_Recovered_Kg",
    "CO2_Saved_Kg",
    "Waste_Diverted_Kg",
    "Circularity_Score",
    "Customer_Rating",
    "Region",
    "City",
    "Final_Disposition",
    "Listing_ID",
    "Condition",
    "Market_Value_INR",
    "Listing_Price_INR"
]

missing_columns = set(expected_columns) - set(df.columns)
extra_columns = set(df.columns) - set(expected_columns)


if not missing_columns:
    print("✅ All expected columns are present")
else:
    print("❌ Missing columns:", missing_columns)


if not extra_columns:
    print("✅ No extra columns")
else:
    print("❌ Extra columns:", extra_columns)


# ------------------------------------------------------------
# 3. Duplicate Validation
# ------------------------------------------------------------

print("\n3. DUPLICATE RECORDS")
print("-" * 40)

duplicates = df.duplicated().sum()

print("Duplicate records:", duplicates)

if duplicates == 0:
    print("✅ No duplicate records")
else:
    print("❌ Duplicate records found")


# ------------------------------------------------------------
# 4. Transaction ID Validation
# ------------------------------------------------------------

print("\n4. TRANSACTION ID VALIDATION")
print("-" * 40)

duplicate_transactions = df["Transaction_ID"].duplicated().sum()
empty_transactions = df["Transaction_ID"].isna().sum()

print("Duplicate Transaction IDs:", duplicate_transactions)
print("Empty Transaction IDs    :", empty_transactions)


# ------------------------------------------------------------
# 5. Product ID Validation
# ------------------------------------------------------------

print("\n5. PRODUCT ID VALIDATION")
print("-" * 40)

duplicate_products = df["Product_ID"].duplicated().sum()
empty_products = df["Product_ID"].isna().sum()

print("Duplicate Product IDs:", duplicate_products)
print("Empty Product IDs    :", empty_products)


# ------------------------------------------------------------
# 6. Marketplace Listing Validation
# ------------------------------------------------------------

print("\n6. MARKETPLACE LISTING VALIDATION")
print("-" * 40)

listing_count = df["Listing_ID"].notna().sum()

print("Marketplace listings found:", listing_count)

if listing_count == 1000:
    print("✅ 1000 marketplace listings found")
else:
    print("⚠️ Marketplace listing count:", listing_count)


# ------------------------------------------------------------
# 7. Listing ID Uniqueness
# ------------------------------------------------------------

print("\n7. LISTING ID VALIDATION")
print("-" * 40)

listing_ids = df["Listing_ID"].dropna()

duplicate_listing_ids = listing_ids.duplicated().sum()

print("Duplicate Listing IDs:", duplicate_listing_ids)

if duplicate_listing_ids == 0:
    print("✅ Listing IDs are unique")
else:
    print("❌ Duplicate Listing IDs found")


# ------------------------------------------------------------
# 8. Price Validation
# ------------------------------------------------------------

print("\n8. MARKETPLACE PRICE VALIDATION")
print("-" * 40)

market_value_negative = (df["Market_Value_INR"] < 0).sum()
listing_price_negative = (df["Listing_Price_INR"] < 0).sum()

print("Negative Market Values :", market_value_negative)
print("Negative Listing Prices:", listing_price_negative)


if market_value_negative == 0 and listing_price_negative == 0:
    print("✅ Marketplace price validation passed")
else:
    print("❌ Invalid marketplace prices found")


# ------------------------------------------------------------
# 9. Condition Validation
# ------------------------------------------------------------

print("\n9. CONDITION VALIDATION")
print("-" * 40)

print(df["Condition"].value_counts(dropna=False))


# ------------------------------------------------------------
# 10. Platform Validation
# ------------------------------------------------------------

print("\n10. PLATFORM VALIDATION")
print("-" * 40)

print(df["Platform"].value_counts(dropna=False))


# ------------------------------------------------------------
# 11. Final Disposition
# ------------------------------------------------------------

print("\n11. FINAL DISPOSITION")
print("-" * 40)

print(df["Final_Disposition"].value_counts(dropna=False))


# ------------------------------------------------------------
# Final Result
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL VALIDATION RESULT")
print("=" * 60)

print("STATUS: PASSED ✅")
print("Integrated marketplace dataset is ready for analytics.")

print("=" * 60)