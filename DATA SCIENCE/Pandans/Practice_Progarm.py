import pandas as pd
data = {
    "ProductID": [101, 102, 103, 104],
    "ProductName": ["Laptop", "Mobile", "Headphones", "Tablet"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics"],
    "City": ["Ahmedabad", "Mumbai", "Delhi", "Bangalore"],
    "Sales": [50000, 30000, 8000, 20000],
    "Profit": [8000, 5000, 1200, 3000],
    "Branch": ["A1", "B2", "C3", "D4"]
}

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df[["ProductName", "Sales"]])
print(df[df["Sales"] > 20000])
print(df[df["Category"] == "Electronics"])






print(df["Sales"].sum())
print(df["Profit"].mean())
print(df["Sales"].max())
print(df["Profit"].min())
print(df.groupby("Category")["Sales"].sum())
df["GST"] = df["Sales"] * 0.18
df["NetProfit"] = df["Sales"] + df["GST"]
print(df)