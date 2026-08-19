import pandas as pd
from pathlib import Path


# ============================================================
# ECHOCHAIN DATA VALIDATION
# ============================================================

print("=" * 70)
print("ECHOCHAIN DATA VALIDATION")
print("=" * 70)


# ------------------------------------------------------------
# 1. File Paths
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEANED_FILE = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "EchoChain_Data_Cleaned.csv"
)


# ------------------------------------------------------------
# 2. Load Cleaned Dataset
# ------------------------------------------------------------

print("\nLoading cleaned dataset...")

df = pd.read_csv(CLEANED_FILE)

print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")


# ------------------------------------------------------------
# 3. Expected Columns
# ------------------------------------------------------------

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


print("\n[1] Checking columns...")

missing_columns = [
    col for col in expected_columns
    if col not in df.columns
]

extra_columns = [
    col for col in df.columns
    if col not in expected_columns
]

if not missing_columns and not extra_columns:
    print("PASS - All expected columns are present.")
else:
    if missing_columns:
        print("Missing columns:", missing_columns)

    if extra_columns:
        print("Extra columns:", extra_columns)


# ------------------------------------------------------------
# 4. Row and Column Count
# ------------------------------------------------------------

print("\n[2] Checking dataset shape...")

if len(df) == 10000:
    print("PASS - Row count = 10,000")
else:
    print(f"WARNING - Row count = {len(df)}")

if len(df.columns) == 33:
    print("PASS - Column count = 33")
else:
    print(f"WARNING - Column count = {len(df.columns)}")


# ------------------------------------------------------------
# 5. Duplicate Records
# ------------------------------------------------------------

print("\n[3] Checking duplicate records...")

duplicate_rows = df.duplicated().sum()

print(f"Duplicate records : {duplicate_rows}")

if duplicate_rows == 0:
    print("PASS - No duplicate records found.")
else:
    print("FAIL - Duplicate records exist.")


# ------------------------------------------------------------
# 6. Transaction_ID Validation
# ------------------------------------------------------------

print("\n[4] Validating Transaction_ID...")

missing_transaction_id = df["Transaction_ID"].isna().sum()
duplicate_transaction_id = df["Transaction_ID"].duplicated().sum()

print(f"Missing Transaction_IDs   : {missing_transaction_id}")
print(f"Duplicate Transaction_IDs : {duplicate_transaction_id}")

if missing_transaction_id == 0 and duplicate_transaction_id == 0:
    print("PASS - Transaction_ID is valid.")
else:
    print("FAIL - Transaction_ID validation failed.")


# ------------------------------------------------------------
# 7. Product_ID Validation
# ------------------------------------------------------------

print("\n[5] Validating Product_ID...")

missing_product_id = df["Product_ID"].isna().sum()
duplicate_product_id = df["Product_ID"].duplicated().sum()

print(f"Missing Product_IDs   : {missing_product_id}")
print(f"Duplicate Product_IDs : {duplicate_product_id}")

if missing_product_id == 0 and duplicate_product_id == 0:
    print("PASS - Product_ID is valid.")
else:
    print("FAIL - Product_ID validation failed.")


# ------------------------------------------------------------
# 8. Date Conversion
# ------------------------------------------------------------

print("\n[6] Validating date columns...")

date_columns = [
    "Purchase_Date",
    "Resale_Date",
    "Recycling_Date"
]

for column in date_columns:

    converted_dates = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    invalid_dates = (
        converted_dates.isna()
        & df[column].notna()
    ).sum()

    print(
        f"{column}: "
        f"Invalid dates = {invalid_dates}"
    )


# ------------------------------------------------------------
# 9. Purchase and Resale Date Validation
# ------------------------------------------------------------

print("\n[7] Validating Purchase_Date and Resale_Date...")

purchase_date = pd.to_datetime(
    df["Purchase_Date"],
    errors="coerce"
)

resale_date = pd.to_datetime(
    df["Resale_Date"],
    errors="coerce"
)

resale_before_purchase = (
    resale_date < purchase_date
).sum()

print(
    f"Resale before Purchase : "
    f"{resale_before_purchase}"
)

if resale_before_purchase == 0:
    print("PASS - Date relationship is valid.")
else:
    print("FAIL - Some resale dates occur before purchase dates.")


# ------------------------------------------------------------
# 10. Recycling Logic Validation
# ------------------------------------------------------------

print("\n[8] Validating recycling logic...")

recycling_date = pd.to_datetime(
    df["Recycling_Date"],
    errors="coerce"
)


# Recycled = Yes but Recycling_Date is missing
recycled_without_date = (
    (df["Recycled"] == "Yes")
    & (recycling_date.isna())
).sum()


# Recycled = No but Recycling_Date exists
not_recycled_with_date = (
    (df["Recycled"] == "No")
    & (recycling_date.notna())
).sum()


print(
    "Recycled = Yes but no Recycling_Date :",
    recycled_without_date
)

print(
    "Recycled = No but Recycling_Date exists :",
    not_recycled_with_date
)


if (
    recycled_without_date == 0
    and not_recycled_with_date == 0
):
    print("PASS - Recycling logic is valid.")
else:
    print("FAIL - Recycling logic has issues.")


# ------------------------------------------------------------
# 11. Refurbishment Logic
# ------------------------------------------------------------

print("\n[9] Validating refurbishment logic...")

invalid_refurbishment = (
    (df["Refurbished"] == "No")
    & (df["Refurbishment_Cost_INR"] > 0)
).sum()

print(
    "Refurbished = No but cost > 0 :",
    invalid_refurbishment
)

if invalid_refurbishment == 0:
    print("PASS - Refurbishment logic is valid.")
else:
    print("FAIL - Refurbishment logic has issues.")


# ------------------------------------------------------------
# 12. Customer Rating Validation
# ------------------------------------------------------------

print("\n[10] Validating Customer_Rating...")

invalid_ratings = (
    (df["Customer_Rating"] < 1)
    | (df["Customer_Rating"] > 5)
).sum()

print(
    "Invalid Customer Ratings :",
    invalid_ratings
)

if invalid_ratings == 0:
    print("PASS - Customer ratings are within 1-5.")
else:
    print("FAIL - Invalid customer ratings found.")


# ------------------------------------------------------------
# 13. Circularity Score Validation
# ------------------------------------------------------------

print("\n[11] Validating Circularity_Score...")

invalid_scores = (
    (df["Circularity_Score"] < 0)
    | (df["Circularity_Score"] > 100)
).sum()

print(
    "Invalid Circularity Scores :",
    invalid_scores
)

if invalid_scores == 0:
    print("PASS - Circularity scores are within 0-100.")
else:
    print("FAIL - Invalid circularity scores found.")


# ------------------------------------------------------------
# 14. Negative Numeric Values
# ------------------------------------------------------------

print("\n[12] Checking negative numeric values...")

numeric_columns = [
    "Original_Price_INR",
    "Current_Market_Value_INR",
    "Resale_Price_INR",
    "Refurbishment_Cost_INR",
    "Repair_Count",
    "Product_Age_Months",
    "Usage_Hours",
    "Material_Recovered_Kg",
    "CO2_Saved_Kg",
    "Waste_Diverted_Kg"
]

negative_values = {}

for column in numeric_columns:

    count = (
        df[column] < 0
    ).sum()

    if count > 0:
        negative_values[column] = count

if not negative_values:
    print("PASS - No negative numeric values found.")
else:
    print("FAIL - Negative values found:")
    print(negative_values)


# ------------------------------------------------------------
# 15. Categorical Validation
# ------------------------------------------------------------

print("\n[13] Validating categorical columns...")


expected_categories = {

    "Condition_at_Resale": [
        "Like New",
        "Good",
        "Fair",
        "Poor"
    ],

    "Seller_Type": [
        "Individual",
        "Business"
    ],

    "Buyer_Type": [
        "Individual",
        "Business"
    ],

    "Refurbished": [
        "Yes",
        "No"
    ],

    "Warranty_Status": [
        "Active",
        "Extended",
        "Expired"
    ],

    "Return_Status": [
        "Returned",
        "Not Returned"
    ],

    "Recycling_Eligible": [
        "Yes",
        "No"
    ],

    "Recycled": [
        "Yes",
        "No"
    ],

    "Final_Disposition": [
        "Resold",
        "Refurbished",
        "Recycled",
        "Landfill"
    ]
}


categorical_errors = {}

for column, allowed_values in expected_categories.items():

    invalid_values = (
        ~df[column].isin(allowed_values)
        & df[column].notna()
    )

    count = invalid_values.sum()

    if count > 0:
        categorical_errors[column] = count


if not categorical_errors:
    print("PASS - All categorical values are valid.")
else:
    print("FAIL - Invalid categorical values found:")
    print(categorical_errors)


# ------------------------------------------------------------
# 16. Missing Value Report
# ------------------------------------------------------------

print("\n[14] Missing value report...")

missing_values = df.isnull().sum()

missing_values = missing_values[
    missing_values > 0
]

if len(missing_values) == 0:
    print("No missing values found.")
else:
    print(missing_values)


# ------------------------------------------------------------
# 17. Final Validation Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL VALIDATION SUMMARY")
print("=" * 70)

print(f"Rows                     : {len(df)}")
print(f"Columns                  : {len(df.columns)}")
print(f"Duplicate rows           : {duplicate_rows}")
print(f"Duplicate Transaction_ID : {duplicate_transaction_id}")
print(f"Duplicate Product_ID     : {duplicate_product_id}")
print(
    f"Resale before Purchase   : "
    f"{resale_before_purchase}"
)
print(
    f"Invalid Recycling Logic  : "
    f"{recycled_without_date + not_recycled_with_date}"
)
print(
    f"Invalid Refurbishment    : "
    f"{invalid_refurbishment}"
)
print(
    f"Invalid Ratings          : "
    f"{invalid_ratings}"
)
print(
    f"Invalid Circularity      : "
    f"{invalid_scores}"
)
print(
    f"Negative Value Issues    : "
    f"{sum(negative_values.values())}"
)
print(
    f"Categorical Issues       : "
    f"{sum(categorical_errors.values())}"
)

print("\nValidation completed successfully.")
print("=" * 70)