import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

df=pd.read_csv(r"D:\Data.csv")


df

x=df.iloc[:,[2,3]]
x
y=df.iloc[:,[4]]
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=10)



from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train_scale=sc.fit_transform(x_train)
x_train_scale=pd.DataFrame(x_train_scale,columns=x_train.columns)
x_train_scale
x_test_scale=sc.transform(x_test)
x_test_scale=pd.DataFrame(x_test_scale,columns=x_test.columns)
x_test_scale


fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(15,5))
ax1.set_title("Before Scaler")
ax1.scatter(x_train["Age"],x_train["EstimatedSalary"])

ax2.set_title("After  Scaler")
ax2.scatter(x_train_scale["Age"],x_train_scale["EstimatedSalary"],color="red")



fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(15,5))

ax1.set_title("Before Scaler")
sns.kdeplot(x_train["Age"],ax=ax1,label="Age")
sns.kdeplot(x_train["EstimatedSalary"],ax=ax1,label="EstimatedSalary")
ax1.legend()

ax2.set_title("After  Scaler")
sns.kdeplot(x_train_scale["Age"],ax=ax2,label="EstimatedSalary")
sns.kdeplot(x_train_scale["EstimatedSalary"],ax=ax2,label="EstimatedSalary")
ax1.legend()
  
fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(15,5))
ax1.set_title("Before Scaler")
sns.kdeplot(x_train["Age"],ax=ax1,label="Age")

ax1.legend()

ax2.set_title("After  Scaler")

sns.kdeplot(x_train_scale["Age"],ax=ax2,label="EstimatedSalary")
ax1.legend()
  
  
fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(15,5))

ax1.set_title("Before Scaler")

sns.kdeplot(x_train["EstimatedSalary"],ax=ax1,label="EstimatedSalary")
ax1.legend()

ax2.set_title("After  Scaler")

sns.kdeplot(x_train_scale["EstimatedSalary"],ax=ax2,label="EstimatedSalary")
ax1.legend()
  

