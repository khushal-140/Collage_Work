import pandas as pd


# Customer Data
customer = pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Customer_Name":["Amit","Riya","John"]
})


# Sales Data
sales = pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Product_ID":[101,102,103],
    "Amount":[5000,3000,7000]
})


# Product Data
product = pd.DataFrame({
    "Product_ID":[101,102,103],
    "Product_Name":["Laptop","Mobile","Tablet"]
})






# Merge Customer + Sales

customer_sales = pd.merge(customer, sales, on="Customer_ID")

# customer_sales=customer.merge(sales,on="Customer_ID")
# print("Customer Purchase Details")
print(customer_sales)

#Join Using Set_index 

# customer.set_index("Customer_ID",inplace=True)
# sales.set_index("Customer_ID",inplace=True)
# print(customer)
# print(sales)
# join=customer.join(sales)
# print(join)

# Join Product Details
customer_sales.set_index("Product_ID", inplace=True)
product.set_index("Product_ID", inplace=True)

final_data = customer_sales.join(product)

print("\nComplete Sales Report")
print(final_data)


# merge=sales.merge(product,on="Product_ID")

# Monthly Sales Data
jan = pd.DataFrame({
    "Product":["Laptop","Mobile"],
    "Sales":[5000,3000]
})

feb = pd.DataFrame({
    "Product_id": [1,2],
    "Sales":[7000,4000]
})
concat=pd.concat([jan,feb],axis=0)
print("Concat")
print(concat)