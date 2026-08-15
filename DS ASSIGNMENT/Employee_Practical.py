import pandas as pd
df=pd.read_csv("employee_performance_payroll_practical.csv")
#Display the first eight rows.
print(df.head(8))
#Find the number of rows and columns
print(df.shape)
#Display all column names.
print(df.columns)
# Inspect data types and non-null counts. 
print(df.info())
#Write two observations about possible data-quality issues. 
print("The DataType of Experience and Rating in Float64 i think in Int64")


#Missing Values 
#Count missing values in each column.
print(df.isnull().sum())


# Display rows containing at least one missing value.
print(df[df.isnull().any(axis=1)])
#Find the total number of missing cells. 
print(df.isnull().sum().sum())






#Treat the missing Experience value using a sensible numerical summary and explain your choice.
df["Experience"]=df["Experience"].fillna(df["Experience"].mode()[0])
#Fill the missing Salary using the median Salary of the Sales department. 
print(df.groupby("Department")["Salary"].median())
df["Salary"]=df["Salary"].fillna(df["Salary"].median())
print(df["Salary"])
print(df.loc[df["Department"]=="Sales","Salary"].median())
print(df)
# Verify that no missing values remain. 
print(df.isnull().sum().sum())
