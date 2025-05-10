import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide", page_title="E-commerce Sales Dashboard")

data_path = os.path.join('..', 'data', 'ecommerce_sales_cleaned.csv')
chart_path = os.path.join('..', 'output', 'charts')

df = pd.read_csv(data_path)

st.title("📦 E-commerce Sales Analyzer")
st.markdown("An interactive dashboard to explore sales performance, product trends, and profitability.")

col1, col2, col3 = st.columns(3)
col1.metric("📈 Total Sales", f"${df['Sales'].sum():,.2f}")
col2.metric("🧾 Total Orders", f"{df['Order ID'].nunique()}")
col3.metric("👥 Unique Customers", f"{df['Customer ID'].nunique()}")

st.markdown("---")

def show_chart(title, filename):
    st.subheader(title)
    img_path = os.path.join(chart_path, filename)
    st.image(img_path, use_column_width=True)

show_chart("Top 10 Selling Products", "top_products.png")
show_chart("Monthly Sales Trend", "monthly_sales.png")

col4, col5 = st.columns(2)
with col4:
    show_chart("Sales by Category", "category_sales.png")
with col5:
    show_chart("Region-wise Sales", "region_sales.png")

show_chart("Profit vs Discount", "profit_discount.png")
show_chart("Segment-wise Revenue", "segment_sales.png")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
