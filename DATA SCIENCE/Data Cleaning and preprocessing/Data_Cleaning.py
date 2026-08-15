import pandas as pd
import numpy as np
#-------------------------Detecting Missing Values
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Age': [25, np.nan, 30, 22, np.nan],
    'City': ['NY', 'LA', 'LA', np.nan, 'SF'],
    'Salary': [50000, 60000, np.nan, 45000, 55000]
}
df = pd.DataFrame(data)
print(df)

# Check for missing values
print(df.isnull())          # Boolean mask (True = missing)
print(df.isnull().sum())    # Count of missing values per column
print(df.isnull().sum().sum())  # Total missing values
print(df.info())            # Shows non-null counts per column


#--------------------------------Removing Missing Values
# Drop rows with ANY missing value
df_dropped = df.dropna()







# Drop rows only if ALL values are missing
df_dropped_all = df.dropna(how='all')

# Drop rows with missing values in specific columns
df_dropped_subset = df.dropna(subset=['Name', 'Age'])

# Drop columns with missing values
df_dropped_cols = df.dropna(axis=1)

# Drop rows with less than N non-null values
df_dropped_thresh = df.dropna(thresh=3)


#------------------------Filling (Imputing) Missing Values
# Fill with a constant
df['City'].fillna('Unknown', inplace=True)

# Fill numeric column with mean/median/mode
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Fill categorical column with mode (most frequent value)
df['Name'].fillna(df['Name'].mode()[0], inplace=True)

# Forward fill / backward fill (useful for time series)
df.fillna(method='ffill', inplace=True)   # carries last valid value forward
df.fillna(method='bfill', inplace=True)   # carries next valid value backward

# Interpolate (estimates values based on surrounding data)
df['Age'] = df['Age'].interpolate(method='linear')

# Fill different columns with different values in one call
df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'}, inplace=True)


#-------------------------------------------Duplicate Detection and Removal
data = {
    'Name': ['Alice', 'Bob', 'Alice', 'David', 'Bob'],
    'Age': [25, 30, 25, 22, 30],
    'City': ['NY', 'LA', 'NY', 'SF', 'LA']
}
df = pd.DataFrame(data)

# Detect duplicates (marks 2nd+ occurrence as True by default)
print(df.duplicated())

# Count duplicate rows
print(df.duplicated().sum())

# Show the actual duplicate rows
print(df[df.duplicated()])

# Check duplicates based on specific column(s) only
print(df.duplicated(subset=['Name']))

# Remove duplicate rows (keeps first occurrence by default)
df_unique = df.drop_duplicates()

# Keep the LAST occurrence instead
df_unique_last = df.drop_duplicates(keep='last')

# Drop ALL duplicates (removes every copy, keeps none)
df_no_dupes = df.drop_duplicates(keep=False)

# Drop duplicates based on subset of columns
df_unique_subset = df.drop_duplicates(subset=['Name', 'City'])

# Apply changes permanently
df.drop_duplicates(inplace=True)

#-----------------------------------------Error Correction
data = {
    'Age': ['25', '30', 'twenty-two', '28'],
    'Price': ['100.5', '200', 'N/A', '150.75']
}
df = pd.DataFrame(data)

# Convert to numeric, force invalid entries to NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
print(df)
# 'twenty-two' and 'N/A' become NaN — now handle them like missing values

#----------------------------------------Fixing Text/Typo Errors
df = pd.DataFrame({'City': ['New York', 'new york', 'NEW YORK', 'LA', 'Los Angeles']})

# Standardize case
df['City'] = df['City'].str.title()



# Map inconsistent spellings/typos to a standard value
city_corrections = {
    'New York': 'New York',
    'La': 'Los Angeles',
    'Los Angeles': 'Los Angeles'
}
df['City'] = df['City'].replace(city_corrections)
print(df)

df = pd.DataFrame({'Gender': ['M', 'Male', 'F', 'Female', 'm', 'f']})
df['Gender'] = df['Gender'].replace({
    'M': 'Male', 'm': 'Male',
    'F': 'Female', 'f': 'Female'
})
print(df)


#-------------------------------Putting It All Together — A Mini Cleaning Pipeline
def clean_dataframe(df):
    df = df.copy()
    
    # 1. Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # 2. Fix data types (coerce invalid entries to NaN)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    
    # 3. Handle missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['City'].fillna('Unknown', inplace=True)
    
    # 4. Standardize text/inconsistent data
    df['City'] = df['City'].str.strip().str.title()
    
    # 5. Fix invalid ranges
    df['Age'] = df['Age'].apply(lambda x: x if 0 <= x <= 120 else np.nan)
    df['Age'].fillna(df['Age'].median(), inplace=True)
    
    return df

df_clean = clean_dataframe(df)


#----------------------------------- Quick Reference Table
# -----------------------------Task	Key Methods
# Detect missing	    isnull(), isna(), .sum()
# Remove missing	    dropna()
# Fill missing	        fillna(), interpolate()
# Detect duplicates	    duplicated()
# Remove duplicates	    drop_duplicates()
# Fix types	            pd.to_numeric(), pd.to_datetime(), astype()
# Fix text errors	    replace(), str.title(), str.strip()
# Fix ranges	        apply() with conditional logic, clip()