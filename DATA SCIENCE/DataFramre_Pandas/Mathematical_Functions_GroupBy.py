import pandas as pd

employee = {
    "ID":[101,102,103,104,105,106],
    "Name":["Khushal","Rahul","Amit","Neha","Priya","Rohan"],
    "Department":["IT","HR","IT","Sales","HR","IT"],
    "Salary":[50000,40000,60000,45000,42000,55000],
    "Age":[22,24,23,25,22,24],
    "Gender":["male","male","male","female","female","female"]
}

df = pd.DataFrame(employee)

print(df["Salary"].sum())

print(df["Age"].sum())

print(df["Salary"].mean())

print(df["Salary"].median())

print(df["Department"].mode()[0])

print(df["Salary"].count())






print(df["Salary"].min())

print(df["Salary"].max())

print(df["Salary"].std())

print(df["Salary"].var())

print(df["Department"].unique())

print(df["Department"].nunique())

print(df["Department"].value_counts())

#Group By
print("---------Group by ---------")

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].max())

print(df.groupby("Department")["Name"].count())

print(df.groupby("Department")["Salary"].agg(["mean","max","min","count"]))






print("---------Group by Multiple Columns---------")

print(df.groupby(["Department","Gender"])["Salary"].mean())

