import pandas as pd

# 1. Load the raw data
df = pd.read_csv("../data/raw/sales_data_raw.csv", encoding="ISO-8859-1")

# 2. Keep only the columns relevant to sales analysis
#    (drop address/contact noise we don't need)
columns_to_keep = [
    "ORDERNUMBER", "ORDERDATE", "QUANTITYORDERED", "PRICEEACH",
    "SALES", "STATUS", "PRODUCTLINE", "PRODUCTCODE",
    "CUSTOMERNAME", "COUNTRY", "TERRITORY", "DEALSIZE",
    "QTR_ID", "MONTH_ID", "YEAR_ID"
]
df = df[columns_to_keep]

# 3. Convert ORDERDATE from text to a real date
#    format="%m/%d/%Y %H:%M" tells pandas exactly how to read it
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], format="%m/%d/%Y %H:%M")

# 4. Fill missing TERRITORY with "Unknown" instead of leaving it blank
#    (better than dropping rows — we don't want to lose real sales data)
df["TERRITORY"] = df["TERRITORY"].fillna("Unknown")

# 5. Standardize text columns: remove extra whitespace, fix casing
df["COUNTRY"] = df["COUNTRY"].str.strip()
df["PRODUCTLINE"] = df["PRODUCTLINE"].str.strip()

# 6. Rename columns to be more readable (lowercase, clear names)
df = df.rename(columns={
    "ORDERNUMBER": "order_id",
    "ORDERDATE": "order_date",
    "QUANTITYORDERED": "quantity",
    "PRICEEACH": "unit_price",
    "SALES": "revenue",
    "STATUS": "status",
    "PRODUCTLINE": "product_category",
    "PRODUCTCODE": "product_code",
    "CUSTOMERNAME": "customer_name",
    "COUNTRY": "country",
    "TERRITORY": "territory",
    "DEALSIZE": "deal_size",
    "QTR_ID": "quarter",
    "MONTH_ID": "month",
    "YEAR_ID": "year"
})

# 7. Sanity check: confirm no unexpected missing values remain
print("Remaining missing values:\n", df.isnull().sum())
print("\nShape after cleaning:", df.shape)
print("\nSample cleaned data:\n", df.head())

# 8. Save the cleaned version to a new file (never overwrite raw data!)
df.to_csv("../data/sales_data_clean.csv", index=False)
print("\nSaved cleaned data to data/sales_data_clean.csv")
