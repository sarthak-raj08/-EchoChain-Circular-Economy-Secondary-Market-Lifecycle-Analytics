import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "EchoChain_Data.csv"
CLEANED_DIR = BASE_DIR / "data" / "cleaned"
CLEANED_FILE = CLEANED_DIR / "EchoChain_Data_Cleaned.csv"


# ============================================================
# 2. LOAD DATA
# ============================================================

print("=" * 70)
print("ECHOCHAIN DATA CLEANING PIPELINE")
print("=" * 70)

print("\nLoading dataset...")

df = pd.read_csv(RAW_FILE)

print(f"Original rows    : {df.shape[0]}")
print(f"Original columns : {df.shape[1]}")


# ============================================================
# 3. CLEAN COLUMN NAMES
# ============================================================

print("\n[1] Cleaning column names...")

df.columns = (
    df.columns
    .str.strip()
)


# ============================================================
# 4. REMOVE DUPLICATE RECORDS
# ============================================================

print("\n[2] Checking duplicate records...")

duplicate_count = df.duplicated().sum()

print(f"Duplicate records found: {duplicate_count}")

if duplicate_count > 0:
    df = df.drop_duplicates()
    print(f"Removed {duplicate_count} duplicate records.")
else:
    print("No duplicate records found.")


# ============================================================
# 5. CLEAN STRING COLUMNS
# ============================================================

print("\n[3] Cleaning text columns...")

string_columns = df.select_dtypes(include=["str"]).columns

for column in string_columns:

    df[column] = (
        df[column]
        .str.strip()
    )

print(f"Cleaned {len(string_columns)} text columns.")


# ============================================================
# 6. CONVERT DATE COLUMNS
# ============================================================

print("\n[4] Converting date columns...")

date_columns = [
    "Purchase_Date",
    "Resale_Date",
    "Recycling_Date"
]

for column in date_columns:

    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    print(
        f"{column}: "
        f"{df[column].notna().sum()} valid dates"
    )


# ============================================================
# 7. CONVERT NUMERIC COLUMNS
# ============================================================

print("\n[5] Converting numeric columns...")

numeric_columns = [
    "Original_Price_INR",
    "Current_Market_Value_INR",
    "Resale_Price_INR",
    "Refurbishment_Cost_INR",
    "Ownership_Cycle",
    "Repair_Count",
    "Product_Age_Months",
    "Usage_Hours",
    "Material_Recovered_Kg",
    "CO2_Saved_Kg",
    "Waste_Diverted_Kg",
    "Circularity_Score",
    "Customer_Rating"
]

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

print(f"Processed {len(numeric_columns)} numeric columns.")


# ============================================================
# 8. STANDARDIZE YES / NO COLUMNS
# ============================================================

print("\n[6] Standardizing Yes/No columns...")

yes_no_columns = [
    "Refurbished",
    "Recycling_Eligible",
    "Recycled"
]

for column in yes_no_columns:

    df[column] = (
        df[column]
        .str.strip()
        .str.title()
    )

print("Yes/No columns standardized.")


# ============================================================
# 9. STANDARDIZE CATEGORICAL TEXT
# ============================================================

print("\n[7] Standardizing categorical columns...")

categorical_columns = [
    "Product_Category",
    "Product_Name",
    "Brand",
    "Condition_at_Resale",
    "Seller_Type",
    "Buyer_Type",
    "Platform",
    "Warranty_Status",
    "Return_Status",
    "Region",
    "City",
    "Final_Disposition"
]

for column in categorical_columns:

    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
    )

print("Categorical values cleaned.")


# ============================================================
# 10. VALIDATE TRANSACTION IDs
# ============================================================

print("\n[8] Validating Transaction_ID...")

transaction_duplicates = df["Transaction_ID"].duplicated().sum()

transaction_nulls = df["Transaction_ID"].isna().sum()

print(f"Duplicate Transaction_IDs : {transaction_duplicates}")
print(f"Missing Transaction_IDs   : {transaction_nulls}")


# ============================================================
# 11. VALIDATE PRODUCT IDs
# ============================================================

print("\n[9] Validating Product_ID...")

product_duplicates = df["Product_ID"].duplicated().sum()

product_nulls = df["Product_ID"].isna().sum()

print(f"Duplicate Product_IDs : {product_duplicates}")
print(f"Missing Product_IDs   : {product_nulls}")


# ============================================================
# 12. VALIDATE DATE LOGIC
# ============================================================

print("\n[10] Validating date relationships...")

invalid_resale_dates = (
    df["Resale_Date"].notna()
    &
    df["Purchase_Date"].notna()
    &
    (df["Resale_Date"] < df["Purchase_Date"])
).sum()

print(
    f"Resale before purchase: "
    f"{invalid_resale_dates}"
)


# ============================================================
# 13. VALIDATE RECYCLING LOGIC
# ============================================================

print("\n[11] Validating recycling logic...")

invalid_recycling_1 = (
    (df["Recycled"] == "Yes")
    & df["Recycling_Date"].isna()
).sum()

invalid_recycling_2 = (
    (df["Recycled"] == "No")
    & df["Recycling_Date"].notna()
).sum()

print(
    f"Recycled = Yes but no Recycling_Date: "
    f"{invalid_recycling_1}"
)

print(
    f"Recycled = No but Recycling_Date exists: "
    f"{invalid_recycling_2}"
)


# ============================================================
# 14. VALIDATE REFURBISHMENT LOGIC
# ============================================================

print("\n[12] Validating refurbishment logic...")

invalid_refurbishment = (
    (df["Refurbished"] == "No")
    &
    (df["Refurbishment_Cost_INR"] > 0)
).sum()

print(
    f"Refurbished = No but cost > 0: "
    f"{invalid_refurbishment}"
)


# ============================================================
# 15. VALIDATE CUSTOMER RATING
# ============================================================

print("\n[13] Validating Customer_Rating...")

invalid_rating = (
    (df["Customer_Rating"] < 1)
    |
    (df["Customer_Rating"] > 5)
).sum()

print(
    f"Invalid ratings: {invalid_rating}"
)


# ============================================================
# 16. VALIDATE CIRCULARITY SCORE
# ============================================================

print("\n[14] Validating Circularity_Score...")

invalid_score = (
    (df["Circularity_Score"] < 0)
    |
    (df["Circularity_Score"] > 100)
).sum()

print(
    f"Invalid circularity scores: {invalid_score}"
)


# ============================================================
# 17. CHECK NEGATIVE VALUES
# ============================================================

print("\n[15] Checking negative numeric values...")

non_negative_columns = [
    "Original_Price_INR",
    "Current_Market_Value_INR",
    "Resale_Price_INR",
    "Refurbishment_Cost_INR",
    "Ownership_Cycle",
    "Repair_Count",
    "Product_Age_Months",
    "Usage_Hours",
    "Material_Recovered_Kg",
    "CO2_Saved_Kg",
    "Waste_Diverted_Kg"
]

for column in non_negative_columns:

    negative_count = (
        df[column] < 0
    ).sum()

    if negative_count > 0:
        print(
            f"{column}: "
            f"{negative_count} negative values"
        )


# ============================================================
# 18. MISSING VALUE REPORT
# ============================================================

print("\n[16] Final missing value report...")

missing_values = df.isna().sum()

missing_values = missing_values[
    missing_values > 0
]

if len(missing_values) == 0:

    print("No missing values found.")

else:

    print(missing_values)


# ============================================================
# 19. SAVE CLEANED DATA
# ============================================================

print("\n[17] Saving cleaned dataset...")

CLEANED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    CLEANED_FILE,
    index=False
)

print(
    f"Cleaned dataset saved to:\n"
    f"{CLEANED_FILE}"
)


# ============================================================
# 20. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)

print(f"Final rows    : {df.shape[0]}")
print(f"Final columns : {df.shape[1]}")

print("\nOutput file:")
print(CLEANED_FILE)

print("\nCleaning pipeline completed successfully.")