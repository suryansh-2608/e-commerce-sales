import pandas as pd
import os

file_path = os.path.join('..', 'data', 'ecommerce_sales_raw.csv')
df = pd.read_csv(file_path)

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

df['Sales Category'] = pd.cut(df['Sales'],
                               bins=[0, 100, 500, 1000],
                               labels=['Low', 'Medium', 'High'])

print("\nMissing Values:\n", df.isnull().sum())

cleaned_path = os.path.join('..', 'data', 'ecommerce_sales_cleaned.csv')
df.to_csv(cleaned_path, index=False)
print(f"\nCleaned data saved to {cleaned_path}")