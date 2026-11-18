# DAX Measures – E-commerce Sales & Profitability Analysis

## 1. Total Sales
```dax
Total Sales = SUM(fact_sales[sales])
```

## 2. Total Profit
```dax
Total Profit = SUM(fact_sales[profit])
```

## 3. Total Quantity
```dax
Total Quantity = SUM(fact_sales[quantity])
```

## 4. Total Orders
```dax
Total Orders = DISTINCTCOUNT(fact_sales[order_id])
```

## 5. Profit Margin
```dax
Profit Margin % =
DIVIDE([Total Profit], [Total Sales], 0) * 100
```

## 6. Average Order Value
```dax
Average Order Value =
DIVIDE([Total Sales], [Total Orders], 0)
```

## 7. Average Discount
```dax
Average Discount % =
AVERAGE(fact_sales[discount]) * 100
```

## 8. Sales per Unit
```dax
Sales per Unit =
DIVIDE([Total Sales], [Total Quantity], 0)
```

## 9. Total Customers
```dax
Total Customers =
DISTINCTCOUNT(fact_sales[customer_key])
```

## 10. Total Loss
```dax
Total Loss =
CALCULATE(
    SUM(fact_sales[profit]),
    fact_sales[profit] < 0
)
```