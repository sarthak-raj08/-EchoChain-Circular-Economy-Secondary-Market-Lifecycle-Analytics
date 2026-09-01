import pandas as pd
import os


# ============================================================
# FILE PATH
# ============================================================

input_file = "data/processed/marketplace_transformed.csv"


# ============================================================
# EXPECTED ECHOCHAIN COLUMNS
# ============================================================

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
    "Final_Disposition"
]


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(input_file)

validation_passed = True


print("=" * 60)
print("TRANSFORMED MARKETPLACE DATA VALIDATION")
print("=" * 60)


# ============================================================
# 1. DATASET SHAPE
# ============================================================

print("\n1. DATASET SHAPE")
print("-" * 40)

print("Rows    :", len(df))
print("Columns :", len(df.columns))

if len(df) != 1000:
    print("❌ Expected 1000 rows")
    validation_passed = False
else:
    print("✅ Row count correct")


if len(df.columns) != 33:
    print("❌ Expected 33 columns")
    validation_passed = False
else:
    print("✅ Column count correct")


# ============================================================
# 2. COLUMN VALIDATION
# ============================================================

print("\n2. COLUMN VALIDATION")
print("-" * 40)

missing_columns = [
    column
    for column in expected_columns
    if column not in df.columns
]

extra_columns = [
    column
    for column in df.columns
    if column not in expected_columns
]


if missing_columns:

    print("❌ Missing columns:")
    for column in missing_columns:
        print(column)

    validation_passed = False

else:

    print("✅ All expected columns are present")


if extra_columns:

    print("\n⚠ Extra columns:")
    for column in extra_columns:
        print(column)

else:

    print("✅ No extra columns")


# ============================================================
# 3. MISSING VALUES
# ============================================================

print("\n3. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values)


# ============================================================
# 4. DUPLICATE RECORDS
# ============================================================

print("\n4. DUPLICATE RECORDS")
print("-" * 40)

duplicate_records = df.duplicated().sum()

print("Duplicate records:", duplicate_records)

if duplicate_records > 0:

    print("❌ Duplicate records found")
    validation_passed = False

else:

    print("✅ No duplicate records")


# ============================================================
# 5. TRANSACTION ID VALIDATION
# ============================================================

print("\n5. TRANSACTION ID VALIDATION")
print("-" * 40)

duplicate_transaction_ids = df["Transaction_ID"].duplicated().sum()

empty_transaction_ids = df["Transaction_ID"].isna().sum()

print("Duplicate Transaction IDs:", duplicate_transaction_ids)
print("Empty Transaction IDs    :", empty_transaction_ids)


if duplicate_transaction_ids == 0 and empty_transaction_ids == 0:

    print("✅ Transaction IDs are unique")

else:

    print("❌ Transaction ID validation failed")
    validation_passed = False


# ============================================================
# 6. PRODUCT ID VALIDATION
# ============================================================

print("\n6. PRODUCT ID VALIDATION")
print("-" * 40)

duplicate_product_ids = df["Product_ID"].duplicated().sum()

empty_product_ids = df["Product_ID"].isna().sum()

print("Duplicate Product IDs:", duplicate_product_ids)
print("Empty Product IDs    :", empty_product_ids)


if duplicate_product_ids == 0 and empty_product_ids == 0:

    print("✅ Product IDs are unique")

else:

    print("❌ Product ID validation failed")
    validation_passed = False


# ============================================================
# 7. PRICE VALIDATION
# ============================================================

print("\n7. PRICE VALIDATION")
print("-" * 40)

price_columns = [
    "Original_Price_INR",
    "Current_Market_Value_INR",
    "Resale_Price_INR"
]

for column in price_columns:

    invalid_prices = (
        pd.to_numeric(df[column], errors="coerce").isna().sum()
    )

    negative_prices = (
        pd.to_numeric(df[column], errors="coerce") < 0
    ).sum()

    print(f"\n{column}")
    print("Invalid values :", invalid_prices)
    print("Negative values:", negative_prices)

    if invalid_prices > 0 or negative_prices > 0:

        print("❌ Price validation failed")
        validation_passed = False

    else:

        print("✅ Price validation passed")


# ============================================================
# 8. RATING VALIDATION
# ============================================================

print("\n8. CUSTOMER RATING VALIDATION")
print("-" * 40)

rating = pd.to_numeric(
    df["Customer_Rating"],
    errors="coerce"
)

invalid_rating = (
    rating.isna()
    | (rating < 1)
    | (rating > 5)
).sum()

print("Invalid ratings:", invalid_rating)

if invalid_rating > 0:

    print("❌ Rating validation failed")
    validation_passed = False

else:

    print("✅ Rating validation passed")


# ============================================================
# 9. CIRCULARITY SCORE VALIDATION
# ============================================================

print("\n9. CIRCULARITY SCORE VALIDATION")
print("-" * 40)

score = pd.to_numeric(
    df["Circularity_Score"],
    errors="coerce"
)

invalid_score = (
    score.isna()
    | (score < 0)
    | (score > 100)
).sum()

print("Invalid circularity scores:", invalid_score)

if invalid_score > 0:

    print("❌ Circularity score validation failed")
    validation_passed = False

else:

    print("✅ Circularity score validation passed")


# ============================================================
# 10. FINAL DISPOSITION
# ============================================================

print("\n10. FINAL DISPOSITION")
print("-" * 40)

print(df["Final_Disposition"].value_counts())


# ============================================================
# FINAL RESULT
# ============================================================

print("\n" + "=" * 60)
print("FINAL VALIDATION RESULT")
print("=" * 60)


if validation_passed:

    print("STATUS: PASSED ✅")
    print("Transformed marketplace dataset is valid.")

else:

    print("STATUS: FAILED ❌")
    print("Please fix the validation errors.")


print("=" * 60)