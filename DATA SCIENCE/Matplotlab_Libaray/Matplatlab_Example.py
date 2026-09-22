import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create Dataset
data = {
    "Customer": ["C101", "C102", "C103", "C104", "C105",
                 "C106", "C107", "C108", "C109", "C110"],

    "Product": ["Laptop", "Mobile", "Headphones", "Laptop", "Mobile",
                "Tablet", "Headphones", "Mobile", "Laptop", "Tablet"],

    "Category": ["Electronics", "Electronics", "Accessories", "Electronics",
                 "Electronics", "Electronics", "Electronics", "Accessories",
                 "Electronics", "Electronics"],

    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar",
              "Mar", "Apr", "Apr", "May", "May"],

    "Sales": [65000, 30000, 5000, 70000, 35000,
              25000, 6000, 32000, 72000, 28000],

    "Quantity": [1, 2, 3, 1, 2,
                 1, 4, 2, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print(df)

# -------------------------------
# 1. Monthly Sales Trend
# -------------------------------

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# -------------------------------
# 2. Average Sales by Product
# -------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Product",
    y="Sales"
)

plt.title("Average Sales by Product")
plt.xlabel("Product")
plt.ylabel("Average Sales")
plt.xticks(rotation=20)
plt.show()


# -------------------------------
# 3. Number of Purchases by Product
# -------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Product"
)

plt.title("Number of Purchases by Product")
plt.xlabel("Product")
plt.ylabel("Number of Purchases")
plt.xticks(rotation=20)
plt.show()


# -------------------------------
# 4. Average Sales by Product
# -------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Product",
    y="Sales"
)

plt.title("Average Sales by Product")
plt.xlabel("Product")
plt.ylabel("Average Sales")
plt.xticks(rotation=20)
plt.show()

# Transcribed Text ContentProductSalesQuantityCustomersPerform the following:Using Matplotlib:

# =>Create a line chart to show monthly sales.
# Create a bar chart to compare product-wise sales.Create a scatter plot to show the relationship between customers and sales
# .Create a histogram to show sales distribution.Create a pie chart to show product-wise sales contribution.Using Seaborn:6. 
# Create a line plot to show the sales trend.7. Create a bar plot to compare average sales by product.8. Create a count plot 
# to show the number of purchases for each product.9. Create a box plot to analyze the distribution of sales by product.
# Would you like me to write the actual Python code using Matplotlib and Seaborn to solve any of these specific exercises?