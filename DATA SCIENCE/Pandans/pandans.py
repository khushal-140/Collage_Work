import pandas as pd


data = {
    "Name": ["Khushal", "Rahul", "Amit", "Rahul"],
    "Marks": [90, None, 88, None],
    "City": ["Diu", "Surat", None, "Surat"]
}

df = pd.DataFrame(data)

print(df.isnull().sum()) #return null row 


df["Marks"]=df["Marks"].fillna(df["Marks"].mean()) #fill the NAN value with mean to find mean propurse 
print(df["Marks"].mean()) #after fillna mean 


df["Marks"] = df["Marks"].fillna(df["Marks"].median()) #fill the NAN value with median to find mean propurse 
print(df["Marks"].median()) #after fillna median

df["City"] = df["City"].fillna(df["City"].mode()[0]) #fill the NAN value with mode to find mean propurse 
print(df["City"].mode()) #after fillna median





print(df["Name"])
print(df["Marks"])
print(df["City"])
df.replace("Diu","Daman")
print(df["City"])
