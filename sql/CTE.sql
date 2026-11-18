use ecommerce_analysis;

-- Find categories generating more than 100,000 in sales.
WITH category_sales AS (
    SELECT
        category,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY category
)
SELECT *
FROM category_sales
WHERE total_sales > 3000;