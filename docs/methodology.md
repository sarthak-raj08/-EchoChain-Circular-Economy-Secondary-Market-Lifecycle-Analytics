# EchoChain Project Methodology

## 1. Introduction

EchoChain follows a structured data-processing methodology to analyze product lifecycle information and secondary-market activity.

The methodology focuses on transforming raw product lifecycle data into validated and analysis-ready datasets through a sequence of cleaning, validation, marketplace integration, analytics, and testing activities.

The major stages are:

1. Data collection
2. Data cleaning
3. Data validation
4. Secondary-market processing
5. Marketplace integration
6. Analytical processing
7. SQL analysis
8. Automated testing
9. Downstream reporting
## 2. Data Collection

The primary dataset is stored in:

`data/raw/EchoChain_Data.csv`

The dataset contains 10,000 product lifecycle records and 33 attributes covering product information, purchasing, resale, refurbishment, recycling, circularity, geographical information, and final disposition.

Secondary-market information is also processed through the Scrapy-based scraping layer located in:

`scrapy/`

The marketplace spider extracts listing-level information such as product title, price, condition, seller, listing ID, and listing date.

The scraping implementation was successfully tested with 20 marketplace listings.

Additional marketplace data is available in:

`data/raw/secondary_market_listings.csv`
## 3. Data Cleaning Methodology

The raw lifecycle dataset is cleaned using:

`scripts/data_cleaning.py`

The cleaning process consists of the following steps:

### 3.1 Duplicate Removal

Exact duplicate records are identified and removed from the dataset.

### 3.2 Data Type Standardization

Date fields are converted into valid date formats, while numeric fields are converted to appropriate numeric data types.

The main date fields include:

- Purchase_Date
- Resale_Date
- Recycling_Date

### 3.3 Text and Categorical Standardization

Column names and text-based fields are stripped of unnecessary whitespace.

Categorical values such as refurbishment, recycling, warranty, and return status are standardized for consistent analysis.

### 3.4 Identifier Validation

Transaction and product identifiers are checked for missing or duplicate values.

### 3.5 Business Rule Validation

The cleaning process checks important lifecycle rules, including:

- Resale dates must not occur before purchase dates.
- Recycled products must have a recycling date.
- Non-recycled products should not have a recycling date.
- Non-refurbished products should not have refurbishment costs.
- Customer ratings must remain within the valid range of 1 to 5.
- Circularity scores must remain within the range of 0 to 100.
- Numeric fields must not contain invalid negative values where negative values are not meaningful.

The cleaned dataset is saved as:

`data/cleaned/EchoChain_Data_Cleaned.csv`
## 4. Data Validation Methodology

After cleaning, the dataset is validated using:

`scripts/data_validation.py`

The validation process verifies:

- Expected column names and schema
- Number of records and columns
- Duplicate records
- Transaction_ID uniqueness
- Product_ID validity
- Date validity and chronology
- Recycling consistency
- Refurbishment consistency
- Customer rating ranges
- Circularity score ranges
- Invalid negative values
- Valid categorical values
- Missing-value patterns

The validation completed successfully for the 10,000-record lifecycle dataset.

The missing `Recycling_Date` values correspond to products that were not recycled and are therefore considered expected missing values rather than data-quality errors.

## 5. Secondary-Market Methodology

EchoChain uses secondary-market data to extend product lifecycle analysis beyond the original point of sale.

### 5.1 Marketplace Dataset Creation

Secondary-market listing data is generated using:

`scripts/create_secondary_market_listings.py`

The resulting dataset contains 1,000 marketplace records and is stored at:

`data/raw/secondary_market_listings.csv`

The records contain marketplace-related information such as:

- Listing ID
- Product ID
- Product name
- Product category
- Condition
- Market value
- Listing price
- Seller type
- Platform
- Region
- Resale information

### 5.2 Marketplace Integration

The marketplace dataset is integrated with the primary lifecycle dataset using:

`scripts/integrate_marketplace_data.py`

The integration uses `Product_ID` as the matching field.

The resulting integrated dataset is stored at:

`data/processed/marketplace_integrated.csv`

The integrated dataset contains 10,000 records and 37 columns.

### 5.3 Marketplace Analytics

Marketplace metrics are generated using:

`scripts/create_marketplace_analytics.py`

The methodology calculates:

- Price difference
- Discount percentage
- Listing-to-market-value ratio
- Pricing category

Additional marketplace analysis is generated using:

`scripts/analyze_marketplace.py`

This supports analysis of marketplace platforms, product categories, product conditions, regions, and discounted products.
## 6. Scraping Methodology

EchoChain uses Scrapy to demonstrate automated collection of secondary-market listing information.

The Scrapy project is located in:

`scrapy/`

The marketplace spider is:

`scrapy/echomarket/spiders/marketplace_spider.py`

The spider extracts the following fields:

- Listing ID
- Product title
- Price
- Condition
- Seller
- Listing date

The extracted items are processed by:

`scrapy/echomarket/pipelines.py`

The `MarketplaceCsvPipeline` writes the collected records to CSV format.

The scraping pipeline was successfully tested with 20 marketplace listings, with all 20 records processed successfully.
## 7. Analytical Methodology

After marketplace integration, analytical metrics are calculated to understand secondary-market pricing and resale opportunities.

The main analytical measures include:

### Price Difference

The difference between the estimated market value and the marketplace listing price.

### Discount Percentage

The percentage difference between market value and listing price, calculated relative to the market value.

### Listing-to-Market Ratio

The ratio between the listing price and the estimated market value.

### Pricing Category

Listings are classified into:

- Below Market Value
- At Market Value
- Above Market Value

Additional analysis is performed across:

- Marketplace platforms
- Product categories
- Product conditions
- Regions
- Product pricing
- Refurbishment
- Final disposition

The resulting analytical datasets are stored under:

`data/processed/marketplace_analysis/`
## 8. Testing Methodology

Automated testing is used to verify the reliability of the implemented data-processing components.

The test suites are located in:

`tests/`

The project contains three main test files:

- `tests/test_data_cleaning.py`
- `tests/test_marketplace.py`
- `tests/test_marketplace_analytics.py`

The tests verify important aspects of the pipeline, including:

- Data-cleaning operations
- Data validation rules
- Marketplace data processing
- Marketplace calculations
- Analytical transformations

The complete test suite is executed using:

`pytest -q`

The current test result is:

`15 passed`

The successful test execution provides verification that the implemented cleaning, marketplace-processing, and analytics functionality behaves as expected.

## 9. Results

The implemented EchoChain pipeline successfully produces validated lifecycle and secondary-market datasets.

The primary lifecycle dataset contains:

- 10,000 records
- 33 columns
- No duplicate transactions
- Valid purchase and resale dates
- Valid circularity scores
- Valid customer ratings
- Consistent recycling and refurbishment information

The secondary-market processing pipeline produces:

- 1,000 marketplace listings
- 10,000 integrated lifecycle records
- 37 columns in the integrated dataset
- 1,000 records available for marketplace analytics

The marketplace analytics identify pricing differences between estimated market value and listing price and classify listings according to their market position.

The automated test suite also completed successfully with:

`15 passed`

These results demonstrate that the implemented data-processing pipeline is functioning correctly and provides analysis-ready datasets for downstream circular-economy reporting.

## 10. Limitations and Future Improvements

The current implementation is a validated analytical prototype. Several areas can be improved for production deployment.

### Current Limitations

- The marketplace dataset is currently based on prepared data for the main analytical pipeline.
- The demonstrated Scrapy scraping layer is separate from the final marketplace integration pipeline.
- Product matching currently uses `Product_ID` for integration.
- Production-scale marketplace ingestion and scheduling are not yet implemented.
- Databricks/Delta Lake and PySpark processing are downstream components of the overall project.
- Power BI is used as the downstream reporting layer.

### Future Improvements

Future versions can:

- Connect live scraping directly to the marketplace analytics pipeline.
- Add scheduled automated data collection.
- Implement more advanced product and SKU matching.
- Integrate Bill of Materials and component-level information.
- Add automated data-quality monitoring.
- Expand secondary-market data sources.
- Automate the complete ingestion-to-reporting workflow.
- Improve real-time or scheduled dashboard updates.

These improvements would help transform the current prototype into a scalable circular-economy lifecycle analytics platform.

