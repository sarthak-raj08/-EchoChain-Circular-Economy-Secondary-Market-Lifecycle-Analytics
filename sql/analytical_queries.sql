-- ============================================================
-- EchoChain Analytical Queries
-- Circular Economy & Secondary Market Lifecycle Analytics
-- ============================================================

-- NOTE:
-- These queries are designed for the cleaned EchoChain lifecycle
-- dataset and should be executed against the final Gold table/view
-- created in the Databricks/Delta Lake layer.
--
-- Logical table name used below:
--     echochain_lifecycle
--
-- Replace echochain_lifecycle with the actual Gold table/view name
-- when deploying these queries.
--
-- Source schema: 33-column EchoChain lifecycle dataset.
-- ============================================================


-- ============================================================
-- 1. Product Lifecycle Overview
-- ============================================================

SELECT
    Product_ID,
    COUNT(*) AS Transaction_Count,
    AVG(Circularity_Score) AS Average_Circularity_Score,
    AVG(Customer_Rating) AS Average_Customer_Rating
FROM echochain_lifecycle
GROUP BY Product_ID
ORDER BY Average_Circularity_Score DESC;


-- ============================================================
-- 2. Average Resale Price by Product
-- ============================================================

SELECT
    Product_ID,
    COUNT(Resale_Date) AS Resale_Count,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR
FROM echochain_lifecycle
WHERE Resale_Date IS NOT NULL
GROUP BY Product_ID
ORDER BY Average_Resale_Price_INR DESC;


-- ============================================================
-- 3. Circularity Performance
-- ============================================================

SELECT
    Product_ID,
    AVG(Circularity_Score) AS Average_Circularity_Score
FROM echochain_lifecycle
GROUP BY Product_ID
ORDER BY Average_Circularity_Score DESC;


-- ============================================================
-- 4. Refurbishment Analysis
-- ============================================================

SELECT
    Refurbished,
    COUNT(*) AS Product_Count,
    AVG(Refurbishment_Cost_INR) AS Average_Refurbishment_Cost_INR
FROM echochain_lifecycle
GROUP BY Refurbished
ORDER BY Product_Count DESC;


-- ============================================================
-- 5. Recycling Analysis
-- ============================================================

SELECT
    Recycled,
    COUNT(*) AS Product_Count,
    SUM(Material_Recovered_Kg) AS Total_Material_Recovered_Kg,
    SUM(CO2_Saved_Kg) AS Total_CO2_Saved_Kg,
    SUM(Waste_Diverted_Kg) AS Total_Waste_Diverted_Kg
FROM echochain_lifecycle
GROUP BY Recycled
ORDER BY Product_Count DESC;


-- ============================================================
-- 6. Final Product Disposition
-- ============================================================

SELECT
    Final_Disposition,
    COUNT(*) AS Product_Count,
    AVG(Circularity_Score) AS Average_Circularity_Score,
    SUM(Waste_Diverted_Kg) AS Total_Waste_Diverted_Kg
FROM echochain_lifecycle
GROUP BY Final_Disposition
ORDER BY Product_Count DESC;


-- ============================================================
-- 7. Product Condition Analysis
-- ============================================================

SELECT
    Condition_at_Resale,
    COUNT(*) AS Product_Count,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR
FROM echochain_lifecycle
WHERE Condition_at_Resale IS NOT NULL
GROUP BY Condition_at_Resale
ORDER BY Average_Resale_Price_INR DESC;


-- ============================================================
-- 8. Warranty Status Analysis
-- ============================================================

SELECT
    Warranty_Status,
    COUNT(*) AS Product_Count,
    AVG(Circularity_Score) AS Average_Circularity_Score
FROM echochain_lifecycle
GROUP BY Warranty_Status
ORDER BY Product_Count DESC;


-- ============================================================
-- 9. Seller Type Analysis
-- ============================================================

SELECT
    Seller_Type,
    COUNT(*) AS Transaction_Count,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR
FROM echochain_lifecycle
WHERE Resale_Price_INR IS NOT NULL
GROUP BY Seller_Type
ORDER BY Average_Resale_Price_INR DESC;


-- ============================================================
-- 10. Buyer Type Analysis
-- ============================================================

SELECT
    Buyer_Type,
    COUNT(*) AS Transaction_Count,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR
FROM echochain_lifecycle
WHERE Resale_Price_INR IS NOT NULL
GROUP BY Buyer_Type
ORDER BY Average_Resale_Price_INR DESC;


-- ============================================================
-- 11. Recycling Eligibility
-- ============================================================

SELECT
    Recycling_Eligible,
    Recycled,
    COUNT(*) AS Product_Count,
    SUM(Material_Recovered_Kg) AS Total_Material_Recovered_Kg
FROM echochain_lifecycle
GROUP BY Recycling_Eligible, Recycled
ORDER BY Recycling_Eligible, Recycled;


-- ============================================================
-- 12. Monthly Resale Analysis
-- ============================================================

SELECT
    YEAR(Resale_Date) AS Resale_Year,
    MONTH(Resale_Date) AS Resale_Month,
    COUNT(*) AS Resale_Count,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR
FROM echochain_lifecycle
WHERE Resale_Date IS NOT NULL
GROUP BY
    YEAR(Resale_Date),
    MONTH(Resale_Date)
ORDER BY
    Resale_Year,
    Resale_Month;


-- ============================================================
-- 13. Monthly Recycling Analysis
-- ============================================================

SELECT
    YEAR(Recycling_Date) AS Recycling_Year,
    MONTH(Recycling_Date) AS Recycling_Month,
    COUNT(*) AS Recycling_Count,
    SUM(Material_Recovered_Kg) AS Material_Recovered_Kg,
    SUM(CO2_Saved_Kg) AS CO2_Saved_Kg,
    SUM(Waste_Diverted_Kg) AS Waste_Diverted_Kg
FROM echochain_lifecycle
WHERE Recycling_Date IS NOT NULL
GROUP BY
    YEAR(Recycling_Date),
    MONTH(Recycling_Date)
ORDER BY
    Recycling_Year,
    Recycling_Month;


-- ============================================================
-- 14. High Circularity Products
-- ============================================================

SELECT
    Product_ID,
    AVG(Circularity_Score) AS Average_Circularity_Score
FROM echochain_lifecycle
GROUP BY Product_ID
HAVING AVG(Circularity_Score) >= 75
ORDER BY Average_Circularity_Score DESC;


-- ============================================================
-- 15. Potential Refurbishment Candidates
-- ============================================================

SELECT
    Product_ID,
    AVG(Circularity_Score) AS Average_Circularity_Score,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR,
    AVG(Refurbishment_Cost_INR) AS Average_Refurbishment_Cost_INR
FROM echochain_lifecycle
WHERE Resale_Price_INR IS NOT NULL
GROUP BY Product_ID
HAVING AVG(Circularity_Score) >= 50
   AND AVG(Resale_Price_INR) > AVG(Refurbishment_Cost_INR)
ORDER BY Average_Resale_Price_INR DESC;


-- ============================================================
-- 16. Executive KPI Summary
-- ============================================================

SELECT
    COUNT(DISTINCT Product_ID) AS Total_Products,
    COUNT(DISTINCT Transaction_ID) AS Total_Transactions,
    AVG(Circularity_Score) AS Average_Circularity_Score,
    AVG(Resale_Price_INR) AS Average_Resale_Price_INR,
    SUM(Material_Recovered_Kg) AS Total_Material_Recovered_Kg,
    SUM(CO2_Saved_Kg) AS Total_CO2_Saved_Kg,
    SUM(Waste_Diverted_Kg) AS Total_Waste_Diverted_Kg,
    AVG(Refurbishment_Cost_INR) AS Average_Refurbishment_Cost_INR
FROM echochain_lifecycle;