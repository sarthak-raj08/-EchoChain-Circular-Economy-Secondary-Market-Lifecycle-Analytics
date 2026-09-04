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