# KPI Definitions
## E-commerce Sales & Profitability Analysis

### 1. Sales Performance KPIs

| KPI Name | Formula | Description |
| Total Sales | SUM(Sales) | Measures total revenue generated from sales. |
| Total Orders | DISTINCTCOUNT(Order ID) | Counts the total number of unique orders. |
| Total Quantity | SUM(Quantity) | Measures the total number of products sold. |

### 2. Profitability KPIs

| KPI Name | Formula | Description |
| Total Profit | SUM(Profit) | Measures the total profit generated. |
| Profit Margin (%) | (Total Profit / Total Sales) × 100 | Measures profit as a percentage of revenue. |

### 3. Customer Performance KPIs

| KPI Name | Formula | Description |
| Total Customers | DISTINCTCOUNT(Customer ID) | Counts the number of unique customers. |
| Average Order Value (AOV) | Total Sales / Total Orders | Measures average revenue generated per order. |

---

## Business Objectives

The main objectives of this project are:

1. **Sales Analysis:** Monitor overall sales performance and identify sales trends.
2. **Profitability Analysis:** Understand profit generation and profit margins.
3. **Product Analysis:** Identify high-performing and low-performing product categories.
4. **Customer Analysis:** Understand customer purchasing patterns and contribution.
5. **Regional Analysis:** Compare sales and profitability across different regions.
6. **Loss Analysis:** Identify products and categories generating negative profits.

---

## KPI Calculation Notes

- Sales and profit are calculated using the transaction-level dataset.
- Orders are counted using distinct Order IDs.
- Customers are counted using distinct Customer IDs.
- Profit margin is calculated using total profit divided by total sales.
- Average Order Value is calculated using total sales divided by unique orders.

## Data Source

**Dataset:** Sample Superstore Dataset

**Tools:** Excel, MySQL, Python, Power BI