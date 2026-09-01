import pandas as pd
import os


# --------------------------------------------------
# 1. File paths
# --------------------------------------------------

input_file = "data/processed/marketplace_cleaned.csv"
output_file = "data/processed/marketplace_transformed.csv"


# --------------------------------------------------
# 2. Read cleaned scraped data
# --------------------------------------------------

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)


# --------------------------------------------------
# 3. Create EchoChain-compatible columns
# --------------------------------------------------

df["Transaction_ID"] = [
    f"SCRAPED_TXN_{i:05d}"
    for i in range(1, len(df) + 1)
]

df["Product_ID"] = [
    f"SCRAPED_PRD_{i:05d}"
    for i in range(1, len(df) + 1)
]

df["Product_Category"] = "Books"

df["Brand"] = "Unknown"

df["Purchase_Date"] = pd.Timestamp.today().strftime("%Y-%m-%d")

df["Original_Price_INR"] = df["Price"] * 90

df["Current_Market_Value_INR"] = (
    df["Original_Price_INR"] * 0.70
)

df["Condition_at_Resale"] = "Good"

df["Ownership_Cycle"] = 1

df["Resale_Date"] = pd.Timestamp.today().strftime("%Y-%m-%d")

df["Resale_Price_INR"] = df["Price"] * 90

df["Seller_Type"] = "Individual"

df["Buyer_Type"] = "Individual"

df["Platform"] = "Books to Scrape"

df["Refurbished"] = False

df["Refurbishment_Cost_INR"] = 0

df["Repair_Count"] = 0

df["Product_Age_Months"] = 0

df["Usage_Hours"] = 0

df["Warranty_Status"] = "Unknown"

df["Return_Status"] = "Unknown"

df["Recycling_Eligible"] = False

df["Recycled"] = False

df["Recycling_Date"] = pd.NaT

df["Material_Recovered_Kg"] = 0

df["CO2_Saved_Kg"] = 0

df["Waste_Diverted_Kg"] = 0

df["Circularity_Score"] = 0

df["Customer_Rating"] = df["Rating"]

df["Region"] = "Unknown"

df["City"] = "Unknown"

df["Final_Disposition"] = "Resold"


# --------------------------------------------------
# 4. Select EchoChain columns
# --------------------------------------------------

final_columns = [
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

df = df[final_columns]


# --------------------------------------------------
# 5. Create output directory if required
# --------------------------------------------------

os.makedirs(
    os.path.dirname(output_file),
    exist_ok=True
)


# --------------------------------------------------
# 6. Save transformed dataset
# --------------------------------------------------

df.to_csv(
    output_file,
    index=False
)


# --------------------------------------------------
# 7. Display result
# --------------------------------------------------

print("\nTransformation completed successfully!")

print("Final Shape:", df.shape)

print("\nFinal Columns:")
for column in df.columns:
    print(column)

print("\nOutput File:")
print(os.path.abspath(output_file))