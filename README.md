# E-commerce Sales & Profitability Analysis

## Project Overview

This project focuses on analyzing e-commerce sales and profitability to identify business trends, evaluate product performance, understand customer purchasing behavior, and generate actionable business insights.

The project uses Microsoft Excel, MySQL, Python, and Power BI to transform raw sales data into meaningful business information.

## Business Problem

E-commerce businesses need to understand their sales performance, profitability, customer behavior, and regional performance to make better business decisions.

This project analyzes historical sales data to identify important trends and opportunities for improving business performance.

## Project Objectives

- Analyze overall sales and profitability.
- Identify top-performing product categories.
- Evaluate regional sales and profit performance.
- Analyze customer purchasing patterns.
- Understand monthly sales trends.
- Identify opportunities to improve profitability.
- Develop an interactive Power BI dashboard.

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Microsoft Excel | Data inspection, cleaning and PivotTables |
| MySQL | Database creation and SQL queries |
| Python | Data cleaning and exploratory data analysis |
| Pandas & NumPy | Data manipulation and numerical analysis |
| Matplotlib & Seaborn | Data visualization |
| Power BI | Data modeling, DAX and interactive dashboards |

## Project Workflow

### 1. Excel – Data Cleaning
- Inspected the dataset.
- Identified missing values and duplicate records.
- Standardized date and numerical formats.
- Used formulas and PivotTables.
- Prepared the cleaned dataset.

### 2. MySQL – Database & Analysis
- Created the project database.
- Imported the cleaned dataset.
- Created fact and dimension tables.
- Practiced filtering, aggregation and joins.
- Used CTEs and window functions.
- Answered business questions using SQL.

### 3. Python – Exploratory Data Analysis
- Loaded and inspected the dataset using Pandas.
- Handled missing values and duplicates.
- Converted numerical and date columns.
- Analyzed sales, profit, categories and customers.
- Created visualizations using Matplotlib and Seaborn.
- Validated results against SQL.

### 4. Power BI – Dashboard Development
- Built the data model and relationships.
- Created DAX measures and KPIs.
- Developed interactive dashboard visuals.
- Added Year, Region, Category and Segment slicers.
- Analyzed sales and profitability performance.
## Power BI Dashboard

![Executive Dashboard](PowerBI/screenshots/executive_dashboard.png)

## Key Dashboard Metrics

Latest recorded Power BI dashboard values:

| KPI | Value |
|---|---:|
| Total Sales | 2.30M |
| Total Profit | 286.40K |
| Total Orders | 5.009K |
| Profit Margin | 12.47% |

## Key Business Insights

- Technology generated the highest sales among the displayed categories.
- Consumer customers contributed the largest share of sales.
- Monthly sales showed fluctuations across the reporting period.
- Customer sales contributions varied across the top customers.
- Regional profit margin calculations require additional validation.

## Repository Structure

```text
ecommerce-sales-performance-analysis/
│
├── data/
├── excel/
├── sql/
├── python/
├── powerbi/
│   └── screenshots/
├── insights/
│   └── business_findings.md
│
└── README.md
```

## How to Reproduce the Project

1. Download the public Sample Superstore dataset from Kaggle or another permitted public source.
2. Open the dataset in Microsoft Excel and perform the documented cleaning steps.
3. Import the cleaned CSV into MySQL.
4. Execute the SQL scripts provided in the sql folder.
5. Open the Python analysis script and install the required libraries.
6. Run the Python analysis using the cleaned dataset.
7. Open the Power BI PBIX file to explore the interactive dashboard.

## Project Limitations

- Results depend on the dataset and selected reporting period.
- Regional profit margin calculations require further validation.
- Historical sales trends do not guarantee future performance.
- Additional cost and discount analysis could improve profitability recommendations.

## Conclusion

This project demonstrates practical data analytics skills using Excel, MySQL, Python, and Power BI.

It showcases the complete analytical workflow, from data cleaning and database management to exploratory analysis, dashboard development, and business recommendations.

## Author

Madhav Mittapelli

Aspiring Data Analyst

Skills: Excel | MySQL | Python | Power BI | Data Cleaning | EDA | SQL | Data Visualization
