import pandas as pd
from pathlib import Path


# ============================================================
# INTEGRATE MARKETPLACE DATA
# ============================================================

print("=" * 60)
print("INTEGRATING MARKETPLACE DATA")
print("=" * 60)


# ------------------------------------------------------------
# File paths
# ------------------------------------------------------------

main_file = Path("./data/raw/EchoChain_Data.csv")
listing_file = Path("./data/raw/secondary_market_listings.csv")

output_file = Path(
    "./data/processed/marketplace_integrated.csv"
)


# ------------------------------------------------------------
# Read datasets
# ------------------------------------------------------------

main_df = pd.read_csv(main_file)
listing_df = pd.read_csv(listing_file)


print("\nMain dataset shape:")
print(main_df.shape)

print("\nListings dataset shape:")
print(listing_df.shape)


# ------------------------------------------------------------
# Referential integrity check
# ------------------------------------------------------------

matching_products = listing_df[
    listing_df["Product_ID"].isin(main_df["Product_ID"])
]

print("\nMatching Product IDs:")
print(len(matching_products))


# ------------------------------------------------------------
# Select marketplace-specific columns
# ------------------------------------------------------------

marketplace_columns = [
    "Listing_ID",
    "Product_ID",
    "Condition",
    "Market_Value_INR",
    "Listing_Price_INR",
]


marketplace_df = listing_df[marketplace_columns].copy()


# ------------------------------------------------------------
# Merge with main dataset
# ------------------------------------------------------------

integrated_df = main_df.merge(
    marketplace_df,
    on="Product_ID",
    how="left"
)


# ------------------------------------------------------------
# Save integrated dataset
# ------------------------------------------------------------

output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)

integrated_df.to_csv(
    output_file,
    index=False
)


# ------------------------------------------------------------
# Final information
# ------------------------------------------------------------

print("\nIntegration completed successfully!")

print("\nFinal dataset shape:")
print(integrated_df.shape)

print("\nFinal columns:")
for column in integrated_df.columns:
    print(column)

print("\nOutput file:")
print(output_file.resolve())

print("=" * 60)
print("PROCESS COMPLETED")
print("=" * 60)