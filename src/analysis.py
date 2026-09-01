import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data_clean.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

territory_revenue = df.groupby("territory")["revenue"].sum().sort_values(ascending=False)

print(territory_revenue)

territory_revenue.plot(kind="bar", figsize=(10, 5), title="Revenue by Territory")
plt.xlabel("Territory")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("../notebooks/territory_revenue.png")

print("Chart saved to notebooks/territory_revenue.png")
