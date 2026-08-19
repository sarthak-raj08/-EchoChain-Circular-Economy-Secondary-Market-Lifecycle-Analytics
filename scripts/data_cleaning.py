import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. File Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "EchoChain_Data.csv"

# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------

df = pd.read_csv(RAW_FILE)

print("=" * 70)
print("ECHCHAIN DATA PROFILING")
print("=" * 70)

# --------------------------------------------------
# 3. Dataset Shape
# --------------------------------------------------

print("\nDataset Shape:")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# --------------------------------------------------
# 4. Column Names
# --------------------------------------------------

print("\nColumns:")
for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")

# --------------------------------------------------
# 5. Data Types
# --------------------------------------------------

print("\nData Types:")
print(df.dtypes)

# --------------------------------------------------
# 6. Missing Values
# --------------------------------------------------

print("\nMissing Values:")
missing = df.isnull().sum()

missing = missing[missing > 0]

if len(missing) == 0:
    print("No missing values found.")
else:
    print(missing)

# --------------------------------------------------
# 7. Duplicate Records
# --------------------------------------------------

print("\nDuplicate Records:")
print(df.duplicated().sum())

# --------------------------------------------------
# 8. Unique Values
# --------------------------------------------------

print("\nUnique Values:")

for column in df.columns:
    print(f"{column}: {df[column].nunique()}")

# --------------------------------------------------
# 9. Numeric Summary
# --------------------------------------------------

print("\nNumeric Summary:")
print(df.describe())

# --------------------------------------------------
# 10. Categorical Summary
# --------------------------------------------------

print("\nCategorical Columns:")

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:
    print(f"\n--- {column} ---")
    print(df[column].value_counts().head(20))

print("\nProfiling completed successfully.")