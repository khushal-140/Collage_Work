import pandas as pd
data = {
    "invoiceid": [101, 102, 103, 104],
    "invoice_date": ["2026-08-01", "2026-08-02", "2026-07-03", "2026-07-04"],
    "amount": [2500, 1800, 3200, 1500]
}

df = pd.DataFrame(data)

print(df)
print("---------DateTime---------")
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
print("---------Date---------")
df["data"]=df["invoice_date"].dt.day
print(df["data"])
print("---------Month---------")
df["month"]=df["invoice_date"].dt.month
print(df["month"])
print("---------Year---------")
df["year"]=df["invoice_date"].dt.year
print(df["year"])






print("---------Weekday---------")
df["weekday"]=df["invoice_date"].dt.weekday
print(df["weekday"])
print("---------Week---------")
df["week"]=df["weekday"].apply(lambda x: "Weekday" if x<=5 else "Weekend")
print(df["week"])
print("---------Groupby---------")
df["group"]=df.groupby("month")["amount"].sum()
print(df["group"])
print("---------Update---------")
print(df)