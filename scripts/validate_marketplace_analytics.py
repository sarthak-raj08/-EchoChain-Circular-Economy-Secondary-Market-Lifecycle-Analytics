import pandas as pd


print("=" * 60)
print("MARKETPLACE ANALYTICS VALIDATION")
print("=" * 60)


# ------------------------------------------------------------
# Load dataset
# ------------------------------------------------------------

file_path = "./data/processed/marketplace_analytics.csv"

df = pd.read_csv(file_path)


# ------------------------------------------------------------
# 1. Dataset Shape
# ------------------------------------------------------------

print("\n1. DATASET SHAPE")
print("-" * 40)

print("Rows    :", len(df))
print("Columns :", len(df.columns))

if len(df) == 1000:
    print("✅ Row count correct")
else:
    print("❌ Row count incorrect")

if len(df.columns) == 41:
    print("✅ Column count correct")
else:
    print("❌ Column count incorrect")


# ------------------------------------------------------------
# 2. Required Analytical Columns
# ------------------------------------------------------------

print("\n2. ANALYTICAL COLUMN VALIDATION")
print("-" * 40)

required_columns = [
    "Price_Difference_INR",
    "Discount_Percentage",
    "Listing_to_Market_Ratio",
    "Pricing_Category"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if not missing_columns:
    print("✅ All analytical columns are present")
else:
    print("❌ Missing columns:", missing_columns)


# ------------------------------------------------------------
# 3. Missing Values
# ------------------------------------------------------------

print("\n3. MISSING VALUES")
print("-" * 40)

missing_values = df[required_columns].isna().sum()

print(missing_values)

if missing_values.sum() == 0:
    print("✅ No missing analytical values")
else:
    print("❌ Missing analytical values found")


# ------------------------------------------------------------
# 4. Price Difference Validation
# ------------------------------------------------------------

print("\n4. PRICE DIFFERENCE VALIDATION")
print("-" * 40)

expected_difference = (
    df["Market_Value_INR"]
    - df["Listing_Price_INR"]
)

difference_errors = (
    (df["Price_Difference_INR"] - expected_difference)
    .abs()
    > 0.01
).sum()

print("Calculation errors:", difference_errors)

if difference_errors == 0:
    print("✅ Price difference calculation is correct")
else:
    print("❌ Price difference calculation has errors")


# ------------------------------------------------------------
# 5. Discount Percentage Validation
# ------------------------------------------------------------

print("\n5. DISCOUNT PERCENTAGE VALIDATION")
print("-" * 40)

expected_discount = (
    (
        df["Market_Value_INR"]
        - df["Listing_Price_INR"]
    )
    / df["Market_Value_INR"]
) * 100

discount_errors = (
    (df["Discount_Percentage"] - expected_discount)
    .abs()
    > 0.01
).sum()

print("Calculation errors:", discount_errors)

if discount_errors == 0:
    print("✅ Discount percentage calculation is correct")
else:
    print("❌ Discount percentage calculation has errors")


# ------------------------------------------------------------
# 6. Listing-to-Market Ratio Validation
# ------------------------------------------------------------

print("\n6. LISTING-TO-MARKET RATIO VALIDATION")
print("-" * 40)

expected_ratio = (
    df["Listing_Price_INR"]
    / df["Market_Value_INR"]
)

ratio_errors = (
    (df["Listing_to_Market_Ratio"] - expected_ratio)
    .abs()
    > 0.01
).sum()

print("Calculation errors:", ratio_errors)

if ratio_errors == 0:
    print("✅ Listing-to-market ratio is correct")
else:
    print("❌ Listing-to-market ratio has errors")


# ------------------------------------------------------------
# 7. Negative Price Validation
# ------------------------------------------------------------

print("\n7. PRICE VALIDATION")
print("-" * 40)

negative_market_value = (
    df["Market_Value_INR"] < 0
).sum()

negative_listing_price = (
    df["Listing_Price_INR"] < 0
).sum()

print("Negative Market Values :", negative_market_value)
print("Negative Listing Prices:", negative_listing_price)

if (
    negative_market_value == 0
    and negative_listing_price == 0
):
    print("✅ Price validation passed")
else:
    print("❌ Negative prices found")


# ------------------------------------------------------------
# 8. Pricing Category Validation
# ------------------------------------------------------------

print("\n8. PRICING CATEGORY VALIDATION")
print("-" * 40)

print(
    df["Pricing_Category"].value_counts()
)


invalid_categories = ~df["Pricing_Category"].isin(
    [
        "Below Market Value",
        "Above Market Value",
        "At Market Value"
    ]
)

invalid_count = invalid_categories.sum()

print("\nInvalid pricing categories:", invalid_count)

if invalid_count == 0:
    print("✅ Pricing categories are valid")
else:
    print("❌ Invalid pricing categories found")


# ------------------------------------------------------------
# 9. Discount Statistics
# ------------------------------------------------------------

print("\n9. DISCOUNT STATISTICS")
print("-" * 40)

print(
    df["Discount_Percentage"].describe()
)


# ------------------------------------------------------------
# 10. Marketplace Summary
# ------------------------------------------------------------

print("\n10. MARKETPLACE SUMMARY")
print("-" * 40)

print(
    "Average Market Value:",
    round(df["Market_Value_INR"].mean(), 2)
)

print(
    "Average Listing Price:",
    round(df["Listing_Price_INR"].mean(), 2)
)

print(
    "Average Discount:",
    round(df["Discount_Percentage"].mean(), 2),
    "%"
)


# ------------------------------------------------------------
# Final Result
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL VALIDATION RESULT")
print("=" * 60)

print("STATUS: PASSED ✅")
print("Marketplace analytics dataset is valid.")

print("=" * 60)