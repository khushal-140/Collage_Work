import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 105, 106],
    "Name": ["Amit", "Riya", "Neha", "Raj", "Karan", "Karan", "Priya"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "HR", "IT"],
    "City": ["Ahmedabad", "Surat", "Rajkot", "Ahmedabad", np.nan, "Surat", "Vadodara"],
    "Salary": [50000, 45000, 70000, 35000, np.nan, 52000, 52000],
    "Grade": ["A", "B", "A", "C", "B", "B", "A"]
})

print(df)


print("Number of Employee in each deparment:")
print(df["Department"].value_counts())

print("Unique City")
print(df["City"].unique())
print("Total nunique Deparment")
print(df["Department"].nunique())




print("Duplicate Record")
print(df["Department"].duplicated())
print(df.duplicated())

df=df.drop_duplicates()
print("After Remove Duplicates Values")
print(df)

print("Missing Values")
print(df.isnull())

print("Missing Values sum")
print(df.isnull().sum())

print("Fill the values wear null ")
df["City"]=df["City"].fillna(df["City"].mode()[0])
print(df)


print("Fill values wear null")
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())

print(df)

# df["Salary"]=df["Salary"].fillna(df["Salary"].mode()[0])
# print(df)

print("Changing Data type")
df["Salary"]=df["Salary"].astype(int)
print(df.dtypes)

print("Random 3 Employee print")
print(df.sample(3))


print("Top 3 higher salary")
print(df.nlargest(3,"Salary"))


print("Bottom 2 lower salary")
print(df.nsmallest(2,"Salary"))

Grade={
    "A":"Excellent",
    "B":"Very Good",
    "C":"Good"
}
df["Perfromance"]=df["Grade"].map(Grade)
print(df)

print("Final DataSet")
df