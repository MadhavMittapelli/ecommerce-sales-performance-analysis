use ecommerce_analysis;

-- create a separate customer summary table

CREATE TABLE customer_summary AS
SELECT
    customer_id,
    customer_name,
    segment
FROM superstore
GROUP BY customer_id, customer_name, segment;
-- Create a customer sales summary
CREATE TABLE customer_sales AS
SELECT
    customer_id,
    SUM(sales) AS total_sales
FROM superstore
GROUP BY customer_id;

-- Join the customer and sales tables.
SELECT
    c.customer_name,
    c.segment,
    s.total_sales
FROM customer_summary c
JOIN customer_sales s
ON c.customer_id = s.customer_id
ORDER BY s.total_sales DESC;