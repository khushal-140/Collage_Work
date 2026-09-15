import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Data_Science"
    
)
cur=conn.cursor()
# cur.execute("CREATE DATABASE IF NOT EXISTS Data_Science")
# print("Database created successfully")
# cur.execute("use Data_Science")
# cur.execute(
#     """create table if not exists customer(
#         id int primary key ,
#         name varchar(20) not null,
#         order_id int not null,
#         address varchar(20) not null
#         )"""
# )
# print("Table created successfully")
# insert_query="""insert into customer(id,name,order_id,address) values(%s,%s,%s,%s)"""
# insert_values=[
#     (1,"John",101,"New York"),
#     (2,"Alice",102,"Los Angeles"),
#     (3,"Bob",103,"Chicago"),
#     (4,"Eve",104,"Houston"),
#     (5,"Charlie",105,"Phoenix")
# ]
# cur.executemany(insert_query,insert_values)

print("Data inserted successfully")
conn.commit()
cur.execute("select *from customer")
data=cur.fetchall()
print("Data fetched successfully")
print("----------------Displaying data from the table Database:--------------")
for row in data:
    print(row)
    
cur.execute("select id,name from customer where order_id=103")
customer_data=cur.fetchall()
print("Data fetched successfully")
print("----------------Displaying data for order ID 103:--------------")
for row in customer_data:
    print(row)
    