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

print(df.loc[0])  # Accessing the first row using loc   
print(df.loc[1,["ProductName","Sales"]])  # Accessing specific columns of the second row using loc
print(df.loc[1:3,["ProductName","Sales"]])  # Accessing specific columns of rows 1 to 2 using loc
print(df.loc[1:3])# Accessing rows 1 to 3 using loc
print(df.loc[df["Sales"]>20000])  # Accessing rows where Sales is greater than 20000 using loc

#iloc is used for accessing rows and columns by integer position. It is primarily used when you want to access data based on its numerical index rather than its label.
print(df.iloc[0])  # Accessing the first row using iloc
print(df.iloc[:,[1, 4]])  # Accessing specific columns of all rows using iloc







print(df.iloc[1:3, [1, 4]])  # Accessing specific columns of rows 1 to 2 using iloc
print(df.iloc[1:3])  # Accessing rows 1 to 2 using iloc
print(df.iloc[1:4,0:3])# Accessing rows 1 to 3 and columns 0 to 2 using iloc
print(df.iloc[1:,[1,4]])  # Accessing specific columns of rows 1 to 2 using iloc