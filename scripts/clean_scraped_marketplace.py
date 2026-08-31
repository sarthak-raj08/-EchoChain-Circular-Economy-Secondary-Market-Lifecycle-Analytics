import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Define file paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "scraped_marketplace.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "marketplace_cleaned.csv"


# --------------------------------------------------
# 2. Create output directory
# --------------------------------------------------

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 3. Read scraped data
# --------------------------------------------------

df = pd.read_csv(RAW_FILE)

print("Original Shape:", df.shape)
print("\nOriginal Columns:")
print(df.columns.tolist())


# --------------------------------------------------
# 4. Remove duplicate records
# --------------------------------------------------

df = df.drop_duplicates()

print("\nAfter removing duplicates:", df.shape)


# --------------------------------------------------
# 5. Clean Product Name
# --------------------------------------------------

df["Product_Name"] = (
    df["Product_Name"]
    .astype(str)
    .str.strip()
)


# --------------------------------------------------
# 6. Clean Price
# --------------------------------------------------

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)


# --------------------------------------------------
# 7. Clean Availability
# --------------------------------------------------

df["Availability"] = (
    df["Availability"]
    .astype(str)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# --------------------------------------------------
# 8. Extract rating
# --------------------------------------------------

rating_mapping = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = (
    df["Rating"]
    .astype(str)
    .str.strip()
    .map(rating_mapping)
)

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

# --------------------------------------------------
# 9. Handle missing values
# --------------------------------------------------

df["Product_Name"] = df["Product_Name"].fillna("Unknown")

df["Availability"] = df["Availability"].fillna("Unknown")

df["Rating"] = df["Rating"].fillna(0).astype(int)


# --------------------------------------------------
# 10. Save cleaned dataset
# --------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# --------------------------------------------------
# 11. Final information
# --------------------------------------------------

print("\nCleaning completed successfully!")

print("Final Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nOutput File:")
print(OUTPUT_FILE)