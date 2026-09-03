# EchoChain Technical Architecture

## 1. Overview

EchoChain is a circular-economy and secondary-market analytics project that combines internal product lifecycle data with secondary-market information to support product resale, refurbishment, recovery, and sustainability analysis.

The implemented project is organized into these main layers:

1. Source data
2. Data cleaning and validation
3. Secondary-market processing
4. Analytics and SQL
5. Downstream processing and visualization
## 2. Source Data

The primary lifecycle dataset is:

`data/raw/EchoChain_Data.csv`

It contains 10,000 records and 33 columns covering:

- Product information
- Purchase and resale dates
- Original and resale prices
- Product condition
- Ownership cycle
- Refurbishment
- Repairs
- Product age and usage
- Warranty and return status
- Recycling information
- Circularity score
- Region and city
- Final disposition

The data dictionary is available at:

`data/raw/Data_Dictionary.csv`

## 3. Data Cleaning and Validation

The primary lifecycle dataset is cleaned using:

`scripts/data_cleaning.py`

The cleaning process includes:

- Removing duplicate records
- Standardizing column names and text values
- Converting date fields to valid date formats
- Converting numeric fields to appropriate numeric types
- Standardizing Yes/No fields
- Validating transaction and product identifiers
- Checking purchase and resale date chronology
- Validating recycling and refurbishment logic
- Validating customer ratings
- Validating circularity scores
- Checking for invalid negative values

The cleaned dataset is generated at:

`data/cleaned/EchoChain_Data_Cleaned.csv`

The cleaned dataset contains 10,000 records and 33 columns.

Validation is performed using:

`scripts/data_validation.py`

The validation process checks schema consistency, duplicates, identifiers, dates, recycling logic, refurbishment logic, ratings, circularity scores, and invalid values.

The validation completed successfully. The only significant missing field is `Recycling_Date` for products that were not recycled, which is expected based on the dataset logic.

## 4. Secondary-Market Processing

EchoChain processes secondary-market information to analyze product resale activity.

The secondary-market dataset is generated using:

`scripts/create_secondary_market_listings.py`

The generated dataset is stored at:

`data/raw/secondary_market_listings.csv`

The dataset contains 1,000 marketplace listings derived from the primary lifecycle data.

The marketplace data is integrated with the primary lifecycle dataset using:

`scripts/integrate_marketplace_data.py`

This process matches marketplace records using `Product_ID` and produces:

`data/processed/marketplace_integrated.csv`

The integrated dataset contains 10,000 records and 37 columns.

Marketplace analytics are then generated using:

`scripts/create_marketplace_analytics.py`

The analytics process calculates:

- Price difference between market value and listing price
- Discount percentage
- Listing-to-market-value ratio
- Pricing category

The resulting analytical dataset is:

`data/processed/marketplace_analytics.csv`

Additional marketplace analysis is generated using:

`scripts/analyze_marketplace.py`

This produces analysis by platform, category, condition, region, and discounted products.

## 5. Scraping Layer

EchoChain includes a Scrapy-based marketplace scraping layer for collecting secondary-market listing information.

The Scrapy project is located in:

`scrapy/`

The marketplace spider is:

`scrapy/echomarket/spiders/marketplace_spider.py`

The spider processes marketplace listing records and extracts:

- Listing ID
- Product title
- Price
- Condition
- Seller
- Listing date

The extracted records are handled by:

`scrapy/echomarket/pipelines.py`

The `MarketplaceCsvPipeline` stores the scraped records as CSV data.

The Scrapy implementation was successfully tested with 20 marketplace listings, with all 20 items successfully processed.

The scraping layer provides a repeatable mechanism for collecting secondary-market data that can later be cleaned, transformed, matched with lifecycle data, and analyzed.

## 6. Analytics Layer

The processed marketplace data is analyzed to identify resale and circular-economy opportunities.

The main analytics script is:

`scripts/analyze_marketplace.py`

The analysis generates separate datasets for:

- Platform performance
- Product category analysis
- Product condition analysis
- Regional analysis
- Top discounted products

The analytical outputs are stored under:

`data/processed/marketplace_analysis/`

Additional marketplace analytics are stored in:

`data/processed/marketplace_analytics.csv`

These outputs support analysis of secondary-market pricing, product conditions, resale opportunities, and marketplace performance.

## 7. SQL Analytical Layer

EchoChain includes SQL queries for performing business-oriented analysis on the lifecycle data.

The analytical SQL queries are stored in:

`sql/analytical_queries.sql`

The SQL layer includes queries for:

- Lifecycle overview
- Resale price analysis
- Circularity score analysis
- Refurbishment analysis
- Recycling analysis
- Final disposition analysis
- Product condition analysis
- Warranty analysis
- Seller and buyer analysis
- Recycling eligibility analysis
- Monthly resale trends
- Monthly recycling trends
- High-circularity products
- Refurbishment candidates
- Executive-level KPIs

These queries provide a structured analytical layer for downstream reporting and can be adapted to the final Gold-layer table or view used by the project.

## 8. Testing and Quality Assurance

EchoChain includes automated tests to verify the correctness of the implemented data-processing pipeline.

The tests are located in:

`tests/`

The test suites cover:

- Data cleaning
- Marketplace data processing
- Marketplace analytics
- Data transformations
- Analytical calculations

The test files include:

- `tests/test_data_cleaning.py`
- `tests/test_marketplace.py`
- `tests/test_marketplace_analytics.py`

The complete test suite was executed using:

`pytest -q`

The current test result is:

`15 passed`

This confirms that the implemented cleaning, marketplace-processing, and analytics functionality passes the available automated tests.

## 9. End-to-End Data Flow

The implemented EchoChain data flow can be summarized as:

1. Primary lifecycle data is stored in `data/raw/EchoChain_Data.csv`.
2. The raw lifecycle data is cleaned using `scripts/data_cleaning.py`.
3. The cleaned dataset is stored in `data/cleaned/EchoChain_Data_Cleaned.csv`.
4. Secondary-market listing data is generated using `scripts/create_secondary_market_listings.py`.
5. Marketplace listings are integrated with lifecycle data using `scripts/integrate_marketplace_data.py`.
6. Marketplace analytical metrics are generated using `scripts/create_marketplace_analytics.py`.
7. Additional marketplace analysis is produced using `scripts/analyze_marketplace.py`.
8. SQL analytical queries are maintained in `sql/analytical_queries.sql`.
9. Automated tests in `tests/` verify the implemented data-processing functionality.
10. The resulting datasets can be consumed by downstream PySpark/Databricks processing and Power BI reporting.

The overall implemented flow is:

`Raw Data → Cleaning → Validation → Marketplace Processing → Integration → Analytics → SQL → Downstream Reporting`

## 10. Implementation Status

The current implementation of EchoChain includes the following completed components:

| Component | Status |
|---|---|
| Primary lifecycle dataset | Completed |
| Data cleaning | Completed |
| Data validation | Completed |
| Secondary-market dataset | Completed |
| Marketplace integration | Completed |
| Marketplace analytics | Completed |
| Scrapy scraping layer | Completed |
| Scraped-data cleaning and transformation | Completed |
| Automated testing | Completed |
| Analytical SQL queries | Completed |
| Git/GitHub version control | Completed |
| Databricks/Delta Lake processing | Downstream component |
| PySpark processing | Downstream component |
| Power BI dashboard | Downstream reporting component |

The implemented Python pipeline has been tested successfully, with all 15 automated tests passing.

PySpark/Databricks processing and Power BI reporting are maintained as downstream components of the overall EchoChain architecture.

## 11. Future Enhancements

The EchoChain architecture can be extended with the following improvements:

- Connect live marketplace scraping directly to the analytics pipeline.
- Add automated scheduled scraping and data ingestion.
- Implement production-grade product and SKU matching.
- Integrate component-level Bill of Materials data.
- Add automated Databricks/Delta Lake ingestion and optimization.
- Expand lifecycle and refurbishment analytics.
- Add real-time or scheduled dashboard refreshes.
- Introduce monitoring and data-quality alerts.
- Add additional marketplace sources for broader secondary-market coverage.
- Improve automation of the complete data pipeline from ingestion to reporting.

These enhancements would allow EchoChain to evolve from a validated analytical prototype into a more automated circular-economy lifecycle analytics platform.