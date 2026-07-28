import pandas as pd


data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "name": [
        "Amit", "Priya", "Rahul", "Neha", "Karan",
        "Sneha", "Vikas", "Anjali", "Rohan", "Pooja",
        "Arjun", "Meera", "Nikhil", "Kavya", "Deepak",
        "Riya", "Sanjay", "Isha", "Manish", "Komal"
    ],


    "city": [
        "Ahmedabad", "Surat", "Rajkot", "Vadodara", "Ahmedabad",
        "Surat", "Mumbai", "Delhi", "Pune", "Rajkot",
        "Mumbai", "Delhi", "Pune", "Ahmedabad", "Surat",
        "Vadodara", "Mumbai", "Delhi", "Pune", "Rajkot"
    ],

    "category": [
        "Electronics", "Furniture", "Clothing", "Electronics", "Furniture",
        "Clothing", "Electronics", "Furniture", "Clothing", "Electronics",
        "Furniture", "Clothing", "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing", "Electronics", "Furniture"
    ],

    "product": [
        "Laptop", "Chair", "T-Shirt", "Mobile", "Table",
        "Jeans", "Headphones", "Sofa", "Jacket", "Tablet",
        "Cupboard", "Shoes", "Smart Watch", "Desk", "Shirt",
        "Camera", "Bed", "Kurta", "Monitor", "Bookshelf"
    ],

    "sales": [
        65000, 12000, 1500, 30000, 18000,
        2500, 5000, 40000, 3500, 28000,
        22000, 4500, 18000, 9000, 2000,
        55000, 35000, 3200, 17000, 14000
    ]
}

df=pd.DataFrame(data)
print("\n List from Columns Want")
print(df[["name","city"]])

print("Diplay The Data 1 to 4")
print(df.iloc[1:5])

print("Diplay The Data 1 to 5")
print(df.loc[1:5])

print("\n Display the details where sales 100000")
print(df[df["sales"]<10000])

print("\n Display the details where category is only give  ")
print(df[df["category"]=="Electronics"])

print("\n And & opertor using and checking condition")
print(df[(df["category"]=="Electronics")&(df["sales"]<10000)] )

print("\n Or | opertor using and checking condition")
print(df[(df["category"]=="Electronics")|(df["sales"]<10000)] )

print("Give Details from Alpabaticle Order with Rerperstive to City Cloumn")
print(df.sort_values("city"))

print("\n Give Details for sales and find hihger salary ")
print(df.sort_values("sales",ascending=False))

print("Group by use and group by use in replting vlaue in colunm and want you want to gorup by column")
print(df.groupby("city")["sales"].sum())

print("Sort by Index")
print(df.sort_index())

print("\n SetIndex with given columns")
df.set_index("customer_id",inplace=True)
#After SetIndex with given Column
print(df)

#want customer details enter custmer Details
#no=int(input("Enter the Number of Custmer:"))
#print(df.loc[no])

print("\n Return Count Mean Medium Satandar Devation Percentage")
print(df.describe())

print("\n Return the Colunns DataType int str float ")
print(df.dtypes)

#--------------Type of Data in Pandas--------------
#1)1-Dimension Srires
#2)2-Dimension  Dataframe

#1)1-Dimension Srires
Series=pd.Series([70,80,90,100],index=[1,2,3,4])
print(Series)

#2)2-Dimension  Dataframe
DataFrame=pd.DataFrame([[10,20,30],
                       [10,20,30],
                       [10,20,30]],columns=["sub1","sub2","sub3"])
print(DataFrame)

