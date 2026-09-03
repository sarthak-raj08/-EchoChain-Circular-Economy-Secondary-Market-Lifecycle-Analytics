# EchoChain: Circular Economy & Secondary Market Lifecycle Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scrapy](https://img.shields.io/badge/Scrapy-Web%20Scraping-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Tests](https://img.shields.io/badge/Tests-15%20Passed-brightgreen)

## Project Overview

**EchoChain** is a circular economy and secondary-market analytics project designed to provide visibility into a product's lifecycle after its initial sale.

Traditional product lifecycle tracking focuses mainly on manufacturing and the first point of sale. Once a product enters the secondary market, information about resale, refurbishment, repair, recycling, and final disposition can become difficult to track.

EchoChain addresses this data visibility gap by combining lifecycle transaction data with secondary-market information to support:

* Product resale analysis
* Secondary-market pricing analysis
* Refurbishment analysis
* Recycling and waste-diversion analysis
* Circularity measurement
* Product lifecycle analytics
* Executive-level sustainability insights

---

## Problem Statement

Manufacturers often have detailed information about a product until it is sold to the first customer. After that point, the product may pass through several ownership and lifecycle stages:

```text
Manufacturer
     |
     v
  Customer
     |
     v
 Secondary Market
     |
     +----> Resale
     |
     +----> Refurbishment
     |
     +----> Repair
     |
     +----> Recycling
     |
     v
Final Disposition
```

Without reliable post-sale data, organizations have limited visibility into:

* How products are resold
* How product value changes over time
* Which products are suitable for refurbishment
* How much material is recovered
* How much waste is diverted from landfill
* The environmental impact of extended product lifecycles

---

## Objectives

The major objectives of EchoChain are to:

1. Clean and validate product lifecycle data.
2. Collect and demonstrate secondary-market listing data.
3. Integrate marketplace information with lifecycle records.
4. Analyze resale prices and market-value differences.
5. Identify pricing opportunities in the secondary market.
6. Analyze product condition, refurbishment, recycling, and final disposition.
7. Provide analytical datasets for downstream SQL and BI analysis.
8. Establish automated data-quality checks through Python tests.

---

## Solution Architecture

The project is organized as a data-processing pipeline:

```text
                    SOURCE DATA
                        |
                        v
              EchoChain_Data.csv
                        |
                        v
              Data Cleaning Layer
                        |
                        v
          EchoChain_Data_Cleaned.csv
                        |
                        v
        Secondary Market Preparation
                        |
                        v
       secondary_market_listings.csv
                        |
                        v
           Marketplace Integration
                        |
                        v
        marketplace_integrated.csv
                        |
                        v
          Marketplace Analytics
                        |
                        v
        marketplace_analytics.csv
                        |
              +---------+---------+
              |                   |
              v                   v
       Analytical SQL       Analysis Reports
              |                   |
              +---------+---------+
                        |
                        v
             Downstream BI Layer
              Power BI / Reporting
```

### Scraping Demonstration Pipeline

A separate Scrapy workflow demonstrates marketplace data collection and transformation:

```text
Scrapy Spider
     |
     v
scraped_marketplace.csv
     |
     v
Data Cleaning
     |
     v
marketplace_cleaned.csv
     |
     v
Transformation
     |
     v
marketplace_transformed.csv
```

The scraping demonstration and the main marketplace analytics pipeline are maintained as separate processing paths.

---

# Key Features

## 1. Data Cleaning

The main lifecycle dataset contains **10,000 records and 33 columns**.

The cleaning process:

* Removes duplicate records
* Standardizes column names and text values
* Converts date fields
* Converts numerical fields to appropriate types
* Standardizes Yes/No fields
* Validates transaction and product IDs
* Validates purchase and resale dates
* Validates recycling information
* Validates refurbishment information
* Validates customer ratings
* Validates circularity scores
* Detects invalid negative values
* Generates a cleaned dataset

Output:

```text
data/cleaned/EchoChain_Data_Cleaned.csv
```

---

## 2. Data Validation

The project includes automated validation scripts covering:

* Schema validation
* Row and column counts
* Duplicate detection
* ID validation
* Date validation
* Recycling logic
* Refurbishment logic
* Rating validation
* Circularity score validation
* Negative-value detection
* Categorical-value validation
* Missing-value reporting

The validation process confirms that the cleaned lifecycle dataset satisfies the defined quality rules.

---

## 3. Secondary-Market Data

The project creates a structured secondary-market dataset from the lifecycle data.

The marketplace dataset contains **1,000 listings** and includes information such as:

* Listing ID
* Product ID
* Product category
* Product name
* Brand
* Condition
* Market value
* Listing price
* Seller type
* Buyer type
* Platform
* Refurbishment status
* Product age
* Customer rating
* Region
* City
* Final disposition

Output:

```text
data/raw/secondary_market_listings.csv
```

---

## 4. Marketplace Integration

Secondary-market records are integrated with the main lifecycle dataset using `Product_ID`.

The integration process produces:

```text
data/processed/marketplace_integrated.csv
```

The integrated dataset contains **10,000 records and 37 columns**, with marketplace information attached to the corresponding lifecycle records.

---

## 5. Marketplace Analytics

The analytics layer calculates additional pricing metrics, including:

### Price Difference

```text
Price Difference =
Market Value - Listing Price
```

### Discount Percentage

```text
Discount Percentage =
((Market Value - Listing Price) / Market Value) × 100
```

### Listing-to-Market Ratio

```text
Listing-to-Market Ratio =
Listing Price / Market Value
```

### Pricing Category

Listings are categorized as:

* Below Market Value
* At Market Value
* Above Market Value

The resulting analytical dataset contains **1,000 marketplace records and 41 columns**.

Output:

```text
data/processed/marketplace_analytics.csv
```

---

# Marketplace Analysis

The project generates several analytical outputs:

```text
data/processed/
|
+-- marketplace_analytics.csv
+-- marketplace_cleaned.csv
+-- marketplace_integrated.csv
+-- marketplace_transformed.csv
|
+-- category_analysis.csv
+-- condition_analysis.csv
+-- marketplace_analysis.csv
+-- platform_analysis.csv
+-- region_analysis.csv
+-- top_discounted_products.csv
|
+-- marketplace_analysis/
    |
    +-- category_analysis.csv
    +-- condition_analysis.csv
    +-- disposition_analysis.csv
    +-- marketplace_summary.csv
    +-- platform_analysis.csv
    +-- pricing_analysis.csv
    +-- refurbishment_analysis.csv
    +-- seller_analysis.csv
    +-- top_market_opportunities.csv
```

These outputs support analysis of:

* Product categories
* Product conditions
* Marketplace platforms
* Regions
* Sellers
* Pricing
* Discounts
* Refurbishment opportunities
* Final disposition
* Market opportunities

---

# Web Scraping

EchoChain includes a **Scrapy-based marketplace scraping demonstration**.

The spider:

```text
scrapy/echomarket/spiders/marketplace_spider.py
```

reads marketplace listing data and produces structured `MarketplaceListingItem` records.

The Scrapy pipeline:

```text
scrapy/echomarket/pipelines.py
```

writes marketplace records to:

```text
data/raw/secondary_market/marketplace_listings.csv
```

The current demonstration successfully processes **20 marketplace listings**.

Run the spider with:

```powershell
cd scrapy
py -m scrapy crawl marketplace
```

---

# Data Transformation

The project also includes a marketplace transformation workflow based on scraped marketplace data:

```text
scraped_marketplace.csv
        |
        v
clean_scraped_marketplace.py
        |
        v
marketplace_cleaned.csv
        |
        v
transform_marketplace_data.py
        |
        v
marketplace_transformed.csv
```

The transformed marketplace dataset follows the EchoChain lifecycle schema and can be validated using:

```powershell
python scripts/validate_transformed_marketplace.py
```

---

# SQL Analytics

The project contains analytical SQL queries in:

```text
sql/analytical_queries.sql
```

The queries cover areas such as:

* Lifecycle overview
* Resale price analysis
* Circularity analysis
* Refurbishment analysis
* Recycling analysis
* Final disposition
* Product condition
* Warranty status
* Seller and buyer analysis
* Recycling eligibility
* Monthly resale trends
* Monthly recycling trends
* High-circularity products
* Refurbishment candidates
* Executive-level KPIs

The SQL layer is designed as an analytical layer that can be adapted to the final Gold dataset or database/view used by the complete project.

---

# Testing

EchoChain includes automated Python tests using `pytest`.

Test files:

```text
tests/
|
+-- test_data_cleaning.py
+-- test_marketplace.py
+-- test_marketplace_analytics.py
```

Run all tests:

```powershell
pytest -q
```

Current result:

```text
15 passed
```

The tests cover data cleaning, marketplace processing, analytical calculations, validation rules, and expected dataset structures.

---

# Project Structure

```text
EchoChain/
|
+-- data/
|   +-- raw/
|   +-- cleaned/
|   +-- processed/
|
+-- docs/
|   +-- architecture.md
|   +-- data_cleaning.md
|   +-- methodology.md
|
+-- notebooks/
|   +-- data_cleaning.ipynb
|
+-- scrapy/
|   +-- scrapy.cfg
|   +-- echomarket/
|       +-- items.py
|       +-- itemloaders.py
|       +-- pipelines.py
|       +-- settings.py
|       +-- spiders/
|
+-- scripts/
|   +-- analyze_marketplace.py
|   +-- clean_scraped_marketplace.py
|   +-- create_marketplace_analytics.py
|   +-- create_secondary_market_listings.py
|   +-- data_cleaning.py
|   +-- data_validation.py
|   +-- integrate_marketplace_data.py
|   +-- transform_marketplace_data.py
|   +-- validate_integrated_marketplace.py
|   +-- validate_marketplace_analytics.py
|   +-- validate_scraped_marketplace.py
|   +-- validate_secondary_market_listings.py
|   +-- validate_transformed_marketplace.py
|
+-- sql/
|   +-- analytical_queries.sql
|
+-- tests/
|   +-- test_data_cleaning.py
|   +-- test_marketplace.py
|   +-- test_marketplace_analytics.py
|
+-- Power BI Dashboard/
|   +-- Dashboard 1.pdf
|   +-- Dashboard 2.pdf
|   +-- EchoChain_PowerBI_Dashboard_Wise_Documentation.docx
|   +-- executive-overview.png
|   +-- product-resale-analytics.png
|
+-- .gitignore
+-- LICENSE
+-- README.md
+-- requirements.txt
```

---

# Technology Stack

| Technology              | Purpose                                |
| ----------------------- | -------------------------------------- |
| Python                  | Data processing and automation         |
| Pandas                  | Data cleaning and analysis             |
| Scrapy                  | Marketplace web-scraping workflow      |
| Pytest                  | Automated testing                      |
| SQL                     | Analytical queries                     |
| Jupyter Notebook        | Exploratory data processing            |
| Databricks / Delta Lake | Project-level lakehouse architecture   |
| PySpark                 | Downstream distributed data processing |
| Power BI                | Dashboard and business intelligence    |

> **Note:** PySpark processing and Power BI dashboard development are downstream/project components and are maintained separately from the Python marketplace-processing workflow documented here.

---

# Installation

Clone the repository:

```powershell
git clone https://github.com/sarthak-raj08/-EchoChain-Circular-Economy-Secondary-Market-Lifecycle-Analytics.git
cd -EchoChain-Circular-Economy-Secondary-Market-Lifecycle-Analytics
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

---

# Requirements

The current Python requirements are:

```text
pandas
scrapy
itemloaders
pytest
```

They are listed in:

```text
requirements.txt
```

---

# Running the Data Pipeline

## Step 1: Clean the Main Dataset

```powershell
python scripts/data_cleaning.py
```

Output:

```text
data/cleaned/EchoChain_Data_Cleaned.csv
```

## Step 2: Validate the Main Dataset

```powershell
python scripts/data_validation.py
```

## Step 3: Create Secondary-Market Listings

```powershell
python scripts/create_secondary_market_listings.py
```

## Step 4: Validate Secondary-Market Listings

```powershell
python scripts/validate_secondary_market_listings.py
```

## Step 5: Integrate Marketplace Data

```powershell
python scripts/integrate_marketplace_data.py
```

## Step 6: Validate Integrated Data

```powershell
python scripts/validate_integrated_marketplace.py
```

## Step 7: Create Marketplace Analytics

```powershell
python scripts/create_marketplace_analytics.py
```

## Step 8: Validate Marketplace Analytics

```powershell
python scripts/validate_marketplace_analytics.py
```

## Step 9: Generate Marketplace Analysis

```powershell
python scripts/analyze_marketplace.py
```

---

# Running the Scrapy Workflow

Navigate to the Scrapy project:

```powershell
cd scrapy
```

Run the marketplace spider:

```powershell
py -m scrapy crawl marketplace
```

The scraped output is written to:

```text
data/raw/secondary_market/marketplace_listings.csv
```

---

# Documentation

Additional project documentation is available in the `docs` directory:

* [Architecture](docs/architecture.md)
* [Data Cleaning](docs/data_cleaning.md)
* [Methodology](docs/methodology.md)

These documents provide additional information about the project architecture, data-processing methodology, cleaning rules, validation strategy, and analytical workflow.

---

# Business Questions

EchoChain is designed to help answer questions such as:

### Product Lifecycle

* How long do products remain in circulation?
* How many ownership cycles do products experience?
* What happens to products after resale?

### Secondary Market

* Which products have the highest resale value?
* Which products are listed below their market value?
* How does condition affect resale pricing?
* Which platforms provide the strongest market opportunities?

### Refurbishment

* Which products are being refurbished?
* What are the associated refurbishment costs?
* Which products could represent refurbishment opportunities?

### Sustainability

* How many products are recycled?
* How much material is recovered?
* How much waste is diverted?
* How much CO2 is saved?
* Which products achieve higher circularity scores?

---

# Circularity and Sustainability

EchoChain connects commercial lifecycle metrics with sustainability indicators.

Important sustainability fields include:

```text
Recycling_Eligible
Recycled
Material_Recovered_Kg
CO2_Saved_Kg
Waste_Diverted_Kg
Circularity_Score
Final_Disposition
```

These fields allow the project to examine the relationship between product lifecycle extension and environmental impact.

---

# Current Implementation Status

| Component                            | Status                       |
| ------------------------------------ | ---------------------------- |
| Main dataset                         | Completed                    |
| Data cleaning                        | Completed                    |
| Data validation                      | Completed                    |
| Secondary-market dataset             | Completed                    |
| Marketplace integration              | Completed                    |
| Marketplace analytics                | Completed                    |
| Marketplace analysis reports         | Completed                    |
| Scrapy demonstration                 | Completed                    |
| Scraped marketplace cleaning         | Completed                    |
| Scraped marketplace transformation   | Completed                    |
| Analytical SQL                       | Completed                    |
| Automated tests                      | Completed                    |
| Project documentation                | Completed                    |
| PySpark processing                   | Downstream project component |
| Power BI dashboards                  | Downstream project component |
| Full production marketplace scraping | Future enhancement           |
| Automated scheduled ingestion        | Future enhancement           |

---

# Limitations

The current implementation has several limitations:

1. The main secondary-market dataset is derived from the project lifecycle data for analytical demonstration.
2. The Scrapy workflow is a marketplace scraping demonstration rather than a production-scale marketplace ingestion system.
3. The scraped marketplace transformation uses generated lifecycle attributes where the source marketplace does not provide equivalent fields.
4. The main marketplace analytics pipeline and the Scrapy demonstration pipeline are separate workflows.
5. Production deployment would require additional monitoring, scheduling, source reliability checks, and marketplace-specific compliance considerations.

---

# Future Enhancements

Potential improvements include:

* Connect live marketplace sources where permitted.
* Add scheduled data ingestion.
* Introduce incremental data processing.
* Implement stronger product/SKU matching.
* Integrate component-level lifecycle information.
* Improve refurbishment opportunity scoring.
* Add advanced depreciation modelling.
* Optimize Delta Lake storage.
* Add automated data-quality monitoring.
* Expand executive dashboard capabilities.
* Add alerts for unusual pricing or lifecycle patterns.

---

# Ethical and Responsible Data Collection

Marketplace data collection should respect:

* Website terms of service
* Robots.txt and crawling policies
* Applicable laws and regulations
* Rate limits
* Privacy requirements
* Data licensing requirements

The project should avoid collecting unnecessary personal information and should use responsible scraping practices.

---

# Learning Outcomes

This project demonstrates practical experience with:

* Python data engineering
* Pandas data cleaning
* Data validation
* Automated testing
* Web scraping with Scrapy
* Data integration
* Marketplace analytics
* SQL analytics
* Data pipeline design
* Circular economy analytics
* Sustainability metrics
* Git and GitHub project management
* Documentation of data-processing workflows

---

# Conclusion

EchoChain demonstrates how product lifecycle and secondary-market data can be combined to provide greater visibility into the circular economy.

The project establishes a structured pipeline for cleaning lifecycle data, processing marketplace information, calculating resale and pricing metrics, validating analytical outputs, and preparing data for downstream business intelligence.

By extending visibility beyond the initial point of sale, EchoChain provides a foundation for analyzing product reuse, refurbishment, resale, recycling, and final disposition while connecting these lifecycle stages with sustainability metrics.

---

## Repository

**GitHub:**
https://github.com/sarthak-raj08/-EchoChain-Circular-Economy-Secondary-Market-Lifecycle-Analytics

---

## License

This project is distributed under the license included in the repository.