from sklearn.preprocessing import LabelEncoder
import pandas as pd
df=pd.read_csv("customer.csv")
print(df)

le=LabelEncoder()
df["purush"]=le.fit_transform(df["purush"])

print(df)
df.to_csv("One_Hot_Encoding.csv")