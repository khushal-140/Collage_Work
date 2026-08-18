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

# --------------------Duplicate Handling 
# Count later exact duplicate rows. 
print(df.duplicated())

# Display all rows involved in exact duplication. 
print(df[df.duplicated()])

#Check repeated Emp_ID values using subset.
print(df[df.duplicated(subset=["Emp_ID"])])

#Explain why repeated Department or City values are not duplicate employee records.
print("Deparment anf City Are Gound Value mean Employee and have from one or mor then one city and department the why")

print(df.shape)
#Remove confirmed exact duplicates and reset the index
print(df.drop_duplicates(inplace=True))
print(df.shape)
#Verify that no exact duplicates remain
print(df.duplicated().sum())
#Report the cleaned number of employees.
print(df)


#------------------------- Sorting
#Sort employees by Salary from highest to lowest.

print("Lowest TO Highest ",df.sort_values(by=("Salary")))

print("Highest TO Lowest ",df.sort_values(by=("Salary"),ascending=False))

# Display the five highest-paid employees.
print(df.sort_values(by=("Salary"),ascending=False).head(5))

#Display the five employees with the highest Rating.
print(df.sort_values("Rating",ascending=False).head(5))

#Sort first by Department and then by Salary from highest to lowest within each department.
print("----------------------------------------")
print(df.sort_values(by=["Department","Salary"],ascending=[True,False]))

#Find the three least-experienced employees. 
print(df.sort_values(by="Experience").head(3))
#Find the highest-paid employee. 
print(df.sort_values(by="Salary",ascending=False).head(1))





# Grouping
#Count employees in each Department.
print(df.groupby("Department")["Name"].count())
#Calculate average Salary by Department.
print(df.groupby("Department")["Salary"].mean())
#Calculate minimum, maximum, and average Salary by Department.
print(df.groupby("Department")["Salary"].agg(["min","max","mean"]))
# Calculate average Rating by Department.
print(df.groupby("Department")["Rating"].mean())
#Calculate average Salary by City
print(df.groupby("City")["Salary"].mean())
#Find maximum Salary in each Department. 
print(df.groupby("Department")["Salary"].max())
# Group by both City and Department and calculate average Salary.
print(df.groupby(["Department","City"])["Salary"].mean())
#Identify the Department with the highest average Salary.
Avg_Mean=df.groupby("Department")["Salary"].mean()
print("Department Name=>",Avg_Mean.idxmax(),"=>",Avg_Mean.max())
# Identify the Department with the highest average Rating. 
Avg_Rate=df.groupby("Department")["Rating"].mean()
print("Department Name=>",Avg_Rate.idxmax(),"=>",Avg_Rate.max())


# Management Questions
#Which department has the largest number of employees?
print(df.groupby("Department")["Name"].count().idxmax())
# Which department has the highest average Salary?
print(df.groupby("Department")["Salary"].mean().idxmax())
#Which department has the highest average Rating
print(df.groupby("Department")["Rating"].mean().idxmax())









# Management Questions
#Which department has the largest number of employees?
print(df.groupby("Department")["Name"].count().idxmax())
# Which department has the highest average Salary?
print(df.groupby("Department")["Salary"].mean().idxmax())
#Which department has the highest average Rating
print(df.groupby("Department")["Rating"].mean().idxmax())
