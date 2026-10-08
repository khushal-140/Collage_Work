import pandas as pd
data={"Student Hours":[1,2,3,4,5,6,7,8,9,10],
      "Marks":[10,20,30,40,50,60,70,80,90,100]}
df=pd.DataFrame(data)
print(df)
print(df.corr())