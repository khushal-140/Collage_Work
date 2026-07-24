import pandas as pd

df=pd.read_excel("info.xlsx")
print("-------Excel File Information-------------")
print(df)
print(df.shape)
print(df.describe())


json=pd.read_json("json.json")
print("-------Json File Infromation------------")
print(json)
print(json.shape)
print(json.columns)
print(json.info())



# Read from dictory and Stored into Dataframe and convert into Excel

# data=[{"No":101,
#      "Name":"I Phone",
#      "Price":7000},
#      {"No":102,
#      "Name":"Readme",
#      "Price":8000},
#      {"No":103,
#      "Name":"Oppo",
#      "Price":9000},
#      {"No":103,
#      "Name":"Viov",
#      "Price":1000}]

# info=pd.DataFrame(data)
# info.to_excel("info.xlsx")