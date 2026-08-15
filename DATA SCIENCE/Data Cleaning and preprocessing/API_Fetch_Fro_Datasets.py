import pandas as pd
import requests

url="https://jsonplaceholder.typicode.com/users";

respondes=requests.get(url)

data=respondes.json()
df=pd.DataFrame(data)


df=df[["id","name","username"]]
df.to_excel("Api.xlsx")
