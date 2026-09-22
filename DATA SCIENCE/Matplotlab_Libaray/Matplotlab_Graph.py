import matplotlib.pylab as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10000, 200, 300, 400, 500]

products=["Laptop","Mobile","Tablet","Desktop","Printer"]
revenue=[10000,20000,30000,40000,50000]
customers=[12000,22000,33000,44000,50000]


#Line Graph
plt.plot(months,sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()

#Bar Graph
plt.bar(products,revenue)
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.title('Revenue Data')
plt.show()







#Scatter Plot
plt.scatter(customers,revenue)
plt.xlabel('Customers')
plt.ylabel('Revenue')
plt.title('Customer vs Revenue')
plt.show()

#Histogram
plt.hist(sales,bins=5)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Sales Distribution')
plt.show()

#pie chart
plt.pie(revenue,labels=products,autopct='%1.1f%%')
plt.title('Revenue Distribution')
plt.show()


import seaborn as sns
#Box Plot
sns.barplot(x=products,y=revenue)
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.title('Revenue Distribution by Product')
plt.show()


