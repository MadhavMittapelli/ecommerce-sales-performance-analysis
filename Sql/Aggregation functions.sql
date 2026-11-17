use ecommerce_analysis;
-- 1.Calculate total sales and profit.
SELECT
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM superstore;

-- 2.Find sales by category.
SELECT category, SUM(sales) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 3.Find the top 10 customers by sales.
select customer_name, sum(sales) as total_sales 
from superstore
group by customer_name
order by total_sales desc
limit 10;

-- 4.Calculate profit by region.
select region, sum(profit) as total_profit
from superstore
group by region
order by total_profit desc;