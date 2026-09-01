import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data_clean.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

product_revenue = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

product_revenue.plot(kind="bar", figsize=(10, 5), title="Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("../notebooks/product_revenue.png")

print("Chart saved to notebooks/product_revenue.png")
