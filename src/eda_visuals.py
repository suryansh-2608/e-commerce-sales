import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

file_path = os.path.join('..', 'data', 'ecommerce_sales_cleaned.csv')
df = pd.read_csv(file_path)

output_dir = os.path.join('..', 'output', 'charts')
os.makedirs(output_dir, exist_ok=True)

top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 10 Selling Products')
plt.xlabel('Sales')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'top_products.png'))
plt.close()

monthly = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
monthly['Month'] = pd.Categorical(monthly['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'],
    ordered=True)
monthly = monthly.sort_values(['Year', 'Month'])
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly, x='Month', y='Sales', hue='Year', marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'monthly_sales.png'))
plt.close()

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Category', y='Sales', palette='Set2')
plt.title('Sales by Category')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'category_sales.png'))
plt.close()

region_sales = df.groupby('Region')['Sales'].sum().sort_values()
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.values, y=region_sales.index, palette='coolwarm')
plt.title('Region-wise Sales')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'region_sales.png'))
plt.close()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category')
plt.title('Profit vs Discount')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'profit_discount.png'))
plt.close()

segment_sales = df.groupby('Segment')['Sales'].sum().sort_values()
plt.figure(figsize=(6, 4))
sns.barplot(x=segment_sales.index, y=segment_sales.values, palette='magma')
plt.title('Segment-wise Revenue')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'segment_sales.png'))
plt.close()

print("📊 EDA visuals saved to /output/charts/")