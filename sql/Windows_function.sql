use ecommerce_analysis;

-- Rank products based on total sales.
WITH product_sales AS (
    SELECT
        product_name,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY product_name
)
SELECT
    product_name,
    total_sales,
    RANK() OVER (
        ORDER BY total_sales DESC
    ) AS sales_rank
FROM product_sales;

-- Rank customers based on profit.

WITH customer_profit AS (
    SELECT
        customer_name,
        SUM(profit) AS total_profit
    FROM superstore
    GROUP BY customer_name
)
SELECT
    customer_name,
    total_profit,
    DENSE_RANK() OVER (
        ORDER BY total_profit DESC
    ) AS profit_rank
FROM customer_profit;