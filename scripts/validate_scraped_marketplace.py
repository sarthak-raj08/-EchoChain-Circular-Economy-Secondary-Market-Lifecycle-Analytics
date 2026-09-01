import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. File path
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "marketplace_cleaned.csv"
)


# --------------------------------------------------
# 2. Read cleaned dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)


print("=" * 60)
print("MARKETPLACE DATA VALIDATION")
print("=" * 60)


# --------------------------------------------------
# 3. Dataset shape
# --------------------------------------------------

print("\n1. DATASET SHAPE")
print("-" * 40)

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# --------------------------------------------------
# 4. Column names
# --------------------------------------------------

print("\n2. COLUMNS")
print("-" * 40)

for column in df.columns:
    print(column)


# --------------------------------------------------
# 5. Missing values
# --------------------------------------------------

print("\n3. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values)


# --------------------------------------------------
# 6. Duplicate records
# --------------------------------------------------

print("\n4. DUPLICATE RECORDS")
print("-" * 40)

duplicate_count = df.duplicated().sum()

print("Duplicate records:", duplicate_count)


# --------------------------------------------------
# 7. Price validation
# --------------------------------------------------

print("\n5. PRICE VALIDATION")
print("-" * 40)

print("Price datatype:", df["Price"].dtype)

invalid_price = df[
    (df["Price"].isnull()) |
    (df["Price"] <= 0)
]

print("Invalid price records:", len(invalid_price))


# --------------------------------------------------
# 8. Product name validation
# --------------------------------------------------

print("\n6. PRODUCT NAME VALIDATION")
print("-" * 40)

empty_product_names = df[
    df["Product_Name"].isnull() |
    (df["Product_Name"].astype(str).str.strip() == "")
]

print("Empty product names:", len(empty_product_names))


# --------------------------------------------------
# 9. Availability validation
# --------------------------------------------------

print("\n7. AVAILABILITY VALIDATION")
print("-" * 40)

print(
    df["Availability"]
    .value_counts()
)


# --------------------------------------------------
# 10. Rating validation
# --------------------------------------------------

print("\n8. RATING VALIDATION")
print("-" * 40)

print(
    df["Rating"]
    .value_counts()
)


# --------------------------------------------------
# 11. URL validation
# --------------------------------------------------

print("\n9. URL VALIDATION")
print("-" * 40)

missing_product_url = df["Product_URL"].isnull().sum()

missing_image_url = df["Image_URL"].isnull().sum()

print("Missing Product URLs:", missing_product_url)
print("Missing Image URLs  :", missing_image_url)


# --------------------------------------------------
# 12. Final validation result
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINAL VALIDATION RESULT")
print("=" * 60)

if (
    len(df) == 1000
    and duplicate_count == 0
    and missing_values.sum() == 0
    and len(invalid_price) == 0
    and len(empty_product_names) == 0
    and missing_product_url == 0
    and missing_image_url == 0
):
    print("STATUS: PASSED")
    print("Dataset is ready for the next transformation step.")

else:
    print("STATUS: REVIEW REQUIRED")
    print("Some validation checks failed.")

print("=" * 60)