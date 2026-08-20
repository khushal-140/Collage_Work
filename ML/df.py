import pandas as pd
df=pd.read_csv("customer.csv")
print(df["Unnamed: 0"])
df.drop(columns="Unnamed: 0",inplace=True)
df.to_csv("customer1.csv")