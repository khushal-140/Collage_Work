import pandas as pd
import sqlite3
conn=sqlite3.connect("Demo.db")
#create Table
conn.execute("""
             create table if not exists Demo1(
             c_id integer,
             c_name Text
             )
             """)
conn.executemany(""" Insert into Demo1 
                 values(?,?)""",
                 [(101,"admin")])
conn.commit()

print(pd.read_sql_query("""select*from Demo1""",conn))