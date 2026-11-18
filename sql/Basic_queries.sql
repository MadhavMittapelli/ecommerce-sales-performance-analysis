use ecommerce_analysis;
SELECT * FROM superstore LIMIT 50;

SELECT COUNT(*) AS total_records
FROM superstore;

-- 1. Find orders with sales greater than 500.
SELECT *
FROM superstore
WHERE sales > 500;

-- 2. Find products from the Technology category.
SELECT *
FROM superstore
WHERE category = 'Technology';

-- 3. Find records with negative profit.
SELECT * FROM superstore
WHERE profit < 0;

SELECT MAX(sales) AS maximum_sale
FROM superstore;