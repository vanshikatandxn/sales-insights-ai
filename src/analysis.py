import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data_clean.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

monthly_revenue = df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()

monthly_revenue.plot(kind="line", figsize=(10, 5), title="Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("../notebooks/monthly_revenue.png")

print("Chart saved to notebooks/monthly_revenue.png")
