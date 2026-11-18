from unicodedata import category

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df = pd.read_csv("Superstore_Cleaned.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    dayfirst=True,
    errors='coerce'
)

for col in ['Sales', 'Profit']:

    # Identify negative values written in parentheses
    negative = df[col].astype(str).str.strip().str.startswith('(')

    # Remove currency symbols, commas and parentheses
    values = df[col].astype(str).str.replace(
        r'[$,()]', '', regex=True
    ).str.strip()

    # Convert into numeric values
    df[col] = pd.to_numeric(values, errors='coerce')

    # Restore negative values
    df.loc[negative, col] = -df.loc[negative, col].abs()

print(df[['Sales', 'Profit']].head(10))

print("\nMissing Values:")
print(df[['Sales', 'Profit']].isnull().sum())

print("\nData Types:")

# Data cleaning using Pandas and NumPy
df1=df.isnull().sum()
df2=(df.isnull().mean() * 100).round(2)


print("Missing Values Count:\n", df1)
print("\nMissing Values Percentage:\n", df2)


print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Correct date formats
df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

df['Ship Date'] = pd.to_datetime(
    df['Ship Date'],
    errors='coerce'
)

# Clean numerical columns
num_cols = ['Sales', 'Profit', 'Quantity', 'Discount']

for col in num_cols:
    df[col] = pd.to_numeric(
        df[col], errors='coerce'
    )

df[num_cols].describe()

# Clean categorical columns
cat_cols = [
    'Category',
    'Sub-Category',
    'Region',
    'Segment',
    'Ship Mode'
]

for col in cat_cols:
    df[col] = df[col].astype('string').str.strip()

# Calculate profit margin

df['Profit Margin'] = np.where(
    df['Sales'] != 0,
    (df['Profit'] / df['Sales']) * 100,
    np.nan
)

# Extract order year
df['Year'] = df['Order Date'].dt.year

# Extract order month
df['Month'] = df['Order Date'].dt.month

# Extract month name
df['Month Name'] = df['Order Date'].dt.strftime('%B')

# Calculate shipping days
df['Shipping Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days

df[['Sales', 'Profit', 'Profit Margin',
    'Year', 'Month', 'Shipping Days']].head()



# — Exploratory Data Analysis (EDA)
# 1.Total sales and profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)

# 2.Sales by category
category_sales = (
    df.groupby('Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)
print(category_sales)

category_sales.plot(
    kind='bar',
    figsize=(8, 5),
    title='Total Sales by Category'
)

plt.ylabel('Sales')
plt.xlabel('Category')
plt.tight_layout()

plt.show()

# 3.Profit by region
region_profit = (
    df.groupby('Region')['Profit']
    .sum()
    .sort_values(ascending=False)
)

print(region_profit)

sns.barplot(
    x=region_profit.index,
    y=region_profit.values
)

plt.title('Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit')
plt.tight_layout()
plt.savefig('profit_by_region.png')
plt.show()

#4. Top 10 products by sales
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

#5. Top 10 most profitable products
top_profit_products = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_profit_products)

# 6.Discount versus profit
sns.scatterplot(
    data=df,
    x='Discount',
    y='Profit'
)

plt.title('Discount vs Profit')
plt.tight_layout()
plt.savefig('sales_vs_profit.png')
plt.show()

# 7.Monthly sales trend
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

monthly_sales = (
    df.set_index('Order Date')
      .resample('MS')['Sales']
      .sum()
)

# Keep the expected variable name used later in exports.
monthly = monthly_sales

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o'
)

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# 8.Sub-category has negative total profit
subcategory_profit = (
    df.groupby('Sub-Category')['Profit']
    .sum()
)

loss_categories = subcategory_profit[
    subcategory_profit < 0
]

print(loss_categories)

# 9.Correlation between sales, profit and discount
correlation = df[
    ['Sales', 'Profit', 'Discount', 'Quantity']
].corr()

print(correlation)

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm'
)

plt.title('Sales and Profit Correlation')
plt.show()


print("Sales:", df['Sales'].sum())
print("Profit:", df['Profit'].sum())
print("Quantity:", df['Quantity'].sum())
print("Orders:", df['Order ID'].nunique())


df.to_csv(
    "cleaned_superstore_python.csv",
    index=False
)

monthly.to_csv(
    "monthly_sales.csv",
    index=False
)

category_sales.to_csv(
    "category_sales.csv"
)