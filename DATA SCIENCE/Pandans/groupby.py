import pandas as pd

data = {
    "Department": ["Electronics", "Electronics", "Clothing", "Clothing",
                   "Grocery", "Electronics", "Grocery", "Clothing"],
    "City": ["Ahmedabad", "Surat", "Ahmedabad", "Rajkot",
             "Surat", "Rajkot", "Ahmedabad", "Surat"],
    "Branch": ["A", "B", "A", "C",
               "B", "A", "C", "B"],
    "Sales": [50000, 30000, 20000, 25000,
              15000, 45000, 18000, 22000],
    "Profit": [8000, 5000, 3000, 4000,
               2500, 7000, 2800, 3500]
}

df = pd.DataFrame(data)


print("Original Dataset")
print(df)

print("\nDepartment-wise Total Sales")
print(df.groupby("Department")["Sales"].sum())


print("\nDepartment-wise Average Sales")
print(df.groupby("Department")["Sales"].mean())


print("\nDepartment-wise Maximum Sales")
print(df.groupby("Department")["Sales"].max())


print("\nDepartment-wise Minimum Sales")
print(df.groupby("Department")["Sales"].min())


print("\nTotal Transactions per Department")
print(df.groupby("Department")["Sales"].count())



print("\nTotal Transactions per Department")
print(df.groupby("Department")["Branch"].count())


print("\nTotal Transactions per Department")
print(df.groupby("Department")["City"].count())

print("\nCity-wise Revenue")
print(df.groupby("City")["Sales"].sum())


print("\nBranch-wise Profit")
print(df.groupby("Branch")["Profit"].sum())


print("\nDepartment-wise Summary Report")
print(df.groupby("Department")["Sales"].agg(["sum", "mean", "min", "max", "count"]))