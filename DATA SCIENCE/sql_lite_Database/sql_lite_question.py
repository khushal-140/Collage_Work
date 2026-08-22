import sqlite3
import pandas as pd
conn=sqlite3.connect("Question.db")
conn.execute("""
             CREATE TABLE IF NOT EXISTS Sales (
    SaleID INTEGER PRIMARY KEY,
    CustomerName TEXT,
    Product TEXT,
    Category TEXT,
    City TEXT,
    Quantity INTEGER,
    Price REAL
    )
             """)
insert_query=[
     (1, 'Rahul', 'Laptop', 'Electronics', 'Ahmedabad', 2, 55000),
    (2, 'Priya', 'Mobile', 'Electronics', 'Mumbai', 3, 25000),
    (3, 'Amit', 'Headphones', 'Electronics', 'Ahmedabad', 5, 3500),
    (4, 'Neha', 'TV', 'Electronics', 'Surat', 1, 45000),
    (5, 'Rohan', 'Tablet', 'Electronics', 'Vadodara', 2, 30000),
    (6, 'Kajal', 'Chair', 'Furniture', 'Ahmedabad', 4, 5000),
    (7, 'Vivek', 'Table', 'Furniture', 'Rajkot', 2, 12000),
    (8, 'Pooja', 'Sofa', 'Furniture', 'Mumbai', 1, 40000),
    (9, 'Arjun', 'Bed', 'Furniture', 'Ahmedabad', 3, 35000),
    (10, 'Sneha', 'Shirt', 'Clothing', 'Surat', 4, 2500),
    (11, 'Karan', 'Jeans', 'Clothing', 'Ahmedabad', 3, 4000),
    (12, 'Meera', 'Jacket', 'Clothing', 'Vadodara', 2, 7000),
    (13, 'Jay', 'Shoes', 'Clothing', 'Rajkot', 5, 6000),
    (14, 'Nisha', 'Refrigerator', 'Electronics', 'Ahmedabad', 1, 60000),
    (15, 'Dhruv', 'Washing Machine', 'Electronics', 'Mumbai', 2, 35000)
]
conn.executemany("insert into sales values(?,?,?,?,?,?,?)",
                 insert_query)

# cur=conn.cursor()
# q=cur.execute("select * from sales ")

# q1="select *from sales"
# print(pd.read_sql_query(q1,conn))

# q2="select CustomerName,Product,Price from sales"
# print(pd.read_sql_query(q2,conn))

# q3="select *from sales where Price>10000"
# print(pd.read_sql_query(q3,conn))

# q4="select *from sales where Quantity>2"
# print(pd.read_sql_query(q4,conn))

# q5="select *from sales where City= 'Ahmedabad'"
# print(pd.read_sql_query(q5,conn))

# q6="select *from sales where Category= 'Electronics'"
# print(pd.read_sql_query(q6,conn))

# q7="select *from sales order by Price "
# print(pd.read_sql_query(q7,conn))

# q8="select *from sales order by Price desc"
# print(pd.read_sql_query(q8,conn))

# q9="select *from sales order by CustomerName "
# print(pd.read_sql_query(q9,conn))

# q10="select *from sales order by Quantity desc "
# print(pd.read_sql_query(q10,conn))

# q11="select *from sales order by City, Price desc  "
# print(pd.read_sql_query(q11,conn))

q11="select *from sales order by City, Price desc  "
print(pd.read_sql_query(q11,conn))