import pandas as pd

df = pd.read_csv("../data/sales_data_clean.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# Filter to only November orders (any year)
november_orders = df[df["order_date"].dt.month == 11]

# Break down November revenue by product category
november_by_product = november_orders.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

print("November revenue by product category:")
print(november_by_product)

# Compare: what % of EACH category's total yearly revenue happens in November?
total_by_product = df.groupby("product_category")["revenue"].sum()
november_share = (november_by_product / total_by_product * 100).sort_values(ascending=False)

print("\n% of each category's total revenue that happens in November:")
print(november_share)
