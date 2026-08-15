import pandas as pd

data = {
    "EmployeeID": ["E101", "E102", "E103", "E104"],
    "Name": ["Asha Patel", "Raj Mehta", "Neha Shah", "Arjun Rao"],
    "Department": ["HR", "IT", "Sales", "Finance"],
    "City": ["Ahmedabad", "Mumbai", "Delhi", "Bangalore"],
    "Age":[20,30,40,50],
    "Salary": [45000, 60000, 55000, 70000],
    "ProfitContribution": [12000, 18500, 20000, 25000]
}

df = pd.DataFrame(data)
print(df)

df["Min_Max_Normalization"]=((df["Age"]-df["Age"].min())/(df["Age"].max()-df["Age"].min()))
df["Z_score_Standardization"]=((df["Age"]-df["Age"].mean())/(df["Age"].std()))


print(df)