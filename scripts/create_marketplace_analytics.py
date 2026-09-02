import pandas as pd
from pathlib import Path


print("=" * 60)
print("CREATING MARKETPLACE ANALYTICS DATASET")
print("=" * 60)


# ------------------------------------------------------------
# Load integrated dataset
# ------------------------------------------------------------

input_file = Path(
    "./data/processed/marketplace_integrated.csv"
)

output_file = Path(
    "./data/processed/marketplace_analytics.csv"
)


df = pd.read_csv(input_file)

print("\nOriginal dataset:")
print(df.shape)


# ------------------------------------------------------------
# Keep only marketplace listings
# ------------------------------------------------------------

analytics_df = df[
    df["Listing_ID"].notna()
].copy()


print("\nMarketplace records:")
print(analytics_df.shape)


# ------------------------------------------------------------
# Calculate price difference
# ------------------------------------------------------------

analytics_df["Price_Difference_INR"] = (
    analytics_df["Market_Value_INR"]
    - analytics_df["Listing_Price_INR"]
)


# ------------------------------------------------------------
# Calculate discount percentage
# ------------------------------------------------------------

analytics_df["Discount_Percentage"] = (
    (
        analytics_df["Market_Value_INR"]
        - analytics_df["Listing_Price_INR"]
    )
    / analytics_df["Market_Value_INR"]
) * 100


# ------------------------------------------------------------
# Calculate listing-to-market ratio
# ------------------------------------------------------------

analytics_df["Listing_to_Market_Ratio"] = (
    analytics_df["Listing_Price_INR"]
    / analytics_df["Market_Value_INR"]
)


# ------------------------------------------------------------
# Create pricing category
# ------------------------------------------------------------

def classify_pricing(row):

    if row["Listing_Price_INR"] < row["Market_Value_INR"]:
        return "Below Market Value"

    elif row["Listing_Price_INR"] > row["Market_Value_INR"]:
        return "Above Market Value"

    else:
        return "At Market Value"


analytics_df["Pricing_Category"] = analytics_df.apply(
    classify_pricing,
    axis=1
)


# ------------------------------------------------------------
# Round calculated values
# ------------------------------------------------------------

analytics_df["Price_Difference_INR"] = (
    analytics_df["Price_Difference_INR"].round(2)
)

analytics_df["Discount_Percentage"] = (
    analytics_df["Discount_Percentage"].round(2)
)

analytics_df["Listing_to_Market_Ratio"] = (
    analytics_df["Listing_to_Market_Ratio"].round(2)
)


# ------------------------------------------------------------
# Save analytics dataset
# ------------------------------------------------------------

output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)

analytics_df.to_csv(
    output_file,
    index=False
)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("\nAnalytics dataset created successfully!")

print("\nFinal Shape:")
print(analytics_df.shape)

print("\nNew analytical columns:")
print("Price_Difference_INR")
print("Discount_Percentage")
print("Listing_to_Market_Ratio")
print("Pricing_Category")

print("\nPricing Category:")
print(
    analytics_df["Pricing_Category"].value_counts()
)

print("\nOutput File:")
print(output_file.resolve())


print("\n" + "=" * 60)
print("PROCESS COMPLETED")
print("=" * 60)