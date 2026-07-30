import pandas as pd,re
df=pd.DataFrame({
    "name":["abc  ","  prq","  xyz","tuv"],
    "email":["abc@gmail.com","pqr@gmail.com","xyz@gmail.com","tuv@gmail.com"]
}) 
print(df)


#Remove Space
print(df["name"].str.strip())

#Upper Case
print(df["name"].str.upper())

#First Title Captical
print(df["name"].str.title())

#Search Specidfic word

print(df[df["name"].str.contains("abc",case=False)])

#Replace Value
replace=df["name"].str.replace("abc","cab",case=False)
print(replace)





#Split Value
df[["Username","Domain"]]=df["email"].str.split("@",expand=True)
print(df[["Username","Domain"]])

#Extract Email Domain @(.+) together  
# This means:

# Find the @ symbol.

# Then capture everything that comes after it (the domain part

df["extract_domain"]=df['email'].str.extract(r'@(.+)')
print(df["extract_domain"])

# Define regex pattern for email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df["valid_email"]=df["email"].str.contains(pattern,regex=True)
print(df[df["valid_email"]])

print(df)