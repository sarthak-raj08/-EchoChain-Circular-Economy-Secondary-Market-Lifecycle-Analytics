# EchoChain Data Cleaning Documentation

## 1. Dataset

Input dataset:

`data/raw/EchoChain_Data.csv`

Cleaned dataset:

`data/cleaned/EchoChain_Data_Cleaned.csv`

Original records: 10,000

Final records: 10,000

Original columns: 33

Final columns: 33

---

## 2. Cleaning Steps

### Column Names
Column names were standardized for consistency.

### Duplicate Records
Duplicate records were checked and none were found.

### Text Cleaning
Whitespace and inconsistent text values were standardized.

### Date Conversion
The following columns were converted to valid date format:

- Purchase_Date
- Resale_Date
- Recycling_Date

### Numeric Conversion
Numeric columns were converted to appropriate numeric data types.

### Yes/No Standardization
The following columns were standardized:

- Refurbished
- Recycling_Eligible
- Recycled

### Categorical Standardization
Categorical values were cleaned and standardized.

---

## 3. Data Validation

### Transaction ID

Duplicate Transaction IDs: 0

Missing Transaction IDs: 0

### Product ID

Duplicate Product IDs: 0

Missing Product IDs: 0

### Date Validation

Resale before Purchase: 0

### Recycling Validation

Recycled = Yes but Recycling_Date missing: 0

Recycled = No but Recycling_Date exists: 0

### Refurbishment Validation

Refurbished = No but Refurbishment Cost > 0: 0

### Customer Rating

Invalid ratings: 0

### Circularity Score

Invalid scores: 0

---

## 4. Missing Values

Recycling_Date contains 8,486 missing values.

These are expected because products with:

`Recycled = No`

do not have a recycling date.

---

## 5. Final Dataset

Rows: 10,000

Columns: 33

The cleaned dataset is stored at:

`data/cleaned/EchoChain_Data_Cleaned.csv`