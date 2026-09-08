# EchoChain – Circular Economy & Secondary Market Lifecycle Analytics

## 📌 Project Overview

EchoChain is a data analytics project designed to analyze product lifecycle data, secondary-market activity, refurbishment, repair, recycling, and circular-economy outcomes.

The project combines the main EchoChain lifecycle dataset with marketplace data collected through a Scrapy-based web scraping pipeline.

The complete workflow covers:

- Web scraping
- Data cleaning
- Data transformation
- Data validation
- Secondary-market listing creation
- Dataset integration
- Marketplace analytics
- Business analysis
- Power BI-ready data preparation

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Collect secondary-market product information.
2. Clean and validate scraped marketplace data.
3. Transform marketplace data into the EchoChain data model.
4. Create a structured secondary-market listings dataset.
5. Integrate marketplace data with the main EchoChain dataset.
6. Calculate marketplace pricing and discount metrics.
7. Analyze marketplace platforms and product categories.
8. Identify pricing opportunities and high-value products.
9. Prepare analytical datasets for Power BI dashboards.
10. Support circular-economy and secondary-market decision making.

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │   Marketplace Data   │
                    │  Books to Scrape     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Scrapy Spider     │
                    │ marketplace_spider   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Scraped Marketplace  │
                    │       CSV            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Cleaning       │
                    │ Pandas Processing    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Transformation    │
                    │ 6 → 33 Columns       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Secondary Market     │
                    │ Listings             │
                    └──────────┬───────────┘
                               │
                               ▼
┌──────────────────────┐       │
│ EchoChain_Data.csv   │───────┤
│ 10,000 Records       │       │
└──────────────────────┘       ▼
                    ┌──────────────────────┐
                    │       Integration     │
                    │ 10,000 + Marketplace │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Marketplace Analytics│
                    │ 41 Analytical Fields │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Python Analysis      │
                    │ Platform / Category  │
                    │ Condition / Region   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Power BI         │
                    │ Analytics Dashboard  │
                    └──────────────────────┘

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Data processing and automation |
| **Pandas** | Data cleaning, transformation, and analysis |
| **Scrapy** | Web scraping and data collection |
| **CSV** | Data storage and data exchange |
| **Power BI** | Data visualization, reporting, and dashboarding |
| **Git** | Version control and source-code management |
| **GitHub** | Source-code collaboration, repository management, and project tracking |


## 🕷️ Web Scraping

A **Scrapy spider** is used to collect marketplace-style product data from a 
legal and publicly available test website.

### 🌐 Test Source

The current test source is:

**Books to Scrape**  
https://books.toscrape.com/

> **Note:** Books to Scrape is a sandbox website specifically designed for 
> web-scraping practice and testing.

### 📌 Data Extracted

The Scrapy spider extracts the following product-level information:

- **Product Name** – Name of the product
- **Price** – Product price
- **Availability** – Current stock/availability status
- **Rating** – Product rating
- **Product URL** – Direct URL of the product page
- **Image URL** – URL of the product image

### 🔄 Pagination

The spider automatically follows the website's **pagination** to collect 
data from multiple pages rather than scraping only the first page.

### 📊 Scraping Output

The scraping process successfully collected:

**1,000 records**

The scraped data is stored in a structured format and can be further processed 
using **Python and Pandas** for cleaning, transformation, and analysis.

### 🔗 Scraping Workflow

```text
Books to Scrape
       ↓
  Scrapy Spider
       ↓
 Pagination Handling
       ↓
 Data Extraction
       ↓
 CSV Dataset
       ↓
 Pandas Cleaning
       ↓
 Analysis & Visualization
       ↓
    Power BI



### Execution Section

The README should also contain the exact commands you have been using.

For example:

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run Scrapy spider
cd scrapy
python -m scrapy crawl marketplace

# Return to project root
cd ..

# Clean scraped data
python .\scripts\clean_scraped_marketplace.py

# Validate scraped data
python .\scripts\validate_scraped_marketplace.py

# Transform marketplace data
python .\scripts\transform_marketplace_data.py

# Validate transformed data
python .\scripts\validate_transformed_marketplace.py

# Create secondary market listings
python .\scripts\create_secondary_market_listings.py

# Validate listings
python .\scripts\validate_secondary_market_listings.py

# Integrate marketplace data
python .\scripts\integrate_marketplace_data.py

# Validate integration
python .\scripts\validate_integrated_marketplace.py

# Create marketplace analytics
python .\scripts\create_marketplace_analytics.py

# Validate analytics
python .\scripts\validate_marketplace_analytics.py

# Run marketplace analysis
python .\scripts\analyze_marketplace.py


# 📊 Current Marketplace Results

Based on the current **1,000 marketplace listings**, the following results were
obtained after processing and analyzing the marketplace dataset.

---

## 📁 Dataset Overview

| Metric | Value |
|--------|-------|
| **Records** | 1,000 |
| **Columns** | 41 |

---

## 💰 Pricing Analysis

| Metric | Value |
|--------|-------|
| **Average Market Value** | ₹49,107.41 |
| **Average Listing Price** | ₹29,292.15 |
| **Average Discount** | 38.49% |

### 📉 Pricing Distribution

The listings were compared against their respective market values.

| Pricing Category | Listings | Percentage |
|------------------|----------|------------|
| **Below Market Value** | 932 | 93.20% |
| **Above Market Value** | 68 | 6.80% |
| **Total** | **1,000** | **100%** |

### 📌 Key Pricing Insight

> **93.20% of marketplace listings are priced below their market value, while
> only 6.80% are priced above market value.**

This indicates that the majority of the analyzed marketplace listings are
offered at prices lower than their estimated market value.

---

## ⭐ Customer Rating Analysis

| Metric | Rating |
|--------|--------|
| **Average Rating** | 3.86 |
| **Highest Rating** | 5.00 |
| **Lowest Rating** | 1.60 |

The dataset shows an overall average customer rating of **3.86**, indicating
generally positive customer feedback across the analyzed listings.

---

## ♻️ Refurbishment Analysis

| Refurbishment Status | Listings | Percentage |
|----------------------|----------|------------|
| **Refurbished** | 374 | 37.40% |
| **Not Refurbished** | 626 | 62.60% |
| **Total** | **1,000** | **100%** |

### 📌 Refurbishment Insight

> **37.40% of the marketplace listings are refurbished, while 62.60% are not
> refurbished.**

This provides an overview of the role of refurbishment within the secondary
marketplace dataset.

---

## 🔄 Final Disposition

The final disposition represents the outcome of the products within the
marketplace lifecycle.

| Final Disposition | Listings | Percentage |
|-------------------|----------|------------|
| **Resold** | 514 | 51.40% |
| **Refurbished** | 300 | 30.00% |
| **Recycled** | 158 | 15.80% |
| **Landfill** | 28 | 2.80% |
| **Total** | **1,000** | **100%** |

### 📌 Final Disposition Insight

> **Resold products represent the largest category at 51.40%, followed by
> refurbished products at 30.00%, recycled products at 15.80%, and landfill
> products at 2.80%.**

---

## 📊 Marketplace Summary

| Category | Key Result |
|----------|------------|
| **Dataset Size** | 1,000 listings |
| **Average Market Value** | ₹49,107.41 |
| **Average Listing Price** | ₹29,292.15 |
| **Average Discount** | 38.49% |
| **Below Market Value** | 93.20% |
| **Average Customer Rating** | 3.86 |
| **Refurbished Products** | 37.40% |
| **Resold Products** | 51.40% |
| **Recycled Products** | 15.80% |
| **Landfill Products** | 2.80% |

---

## 💡 Key Business Insights

1. **Strong Pricing Opportunity**  
   93.20% of listings are below their estimated market value, highlighting a
   significant pricing gap in the secondary marketplace.

2. **Healthy Customer Feedback**  
   The average customer rating is **3.86/5**, suggesting generally positive
   customer satisfaction.

3. **Significant Refurbishment Activity**  
   **37.40%** of listings are refurbished, demonstrating the importance of
   refurbishment in extending product lifecycles.

4. **High Resale Rate**  
   **51.40%** of products are ultimately resold, showing strong potential for
   secondary-market circulation.

5. **Low Landfill Share**  
   Only **2.80%** of products reach landfill, indicating that most products
   continue through resale, refurbishment, or recycling pathways.

---

## 🔗 Marketplace Analytics Flow

```text
1,000 Marketplace Listings
            ↓
     Data Cleaning
            ↓
      Data Validation
            ↓
      Pricing Analysis
            ↓
    Customer Rating Analysis
            ↓
   Refurbishment Analysis
            ↓
     Final Disposition
            ↓
     Business Insights
            ↓
       Power BI Dashboard