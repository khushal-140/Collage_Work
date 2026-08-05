import pandas as pd
data = {
    "invoiceid": [101, 102, 103, 104],
    "invoice_date": ["2026-08-01", "2026-08-02", "2026-07-03", "2026-07-04"],
    "amount": [2500, 1800, 3200, 1500]
}

df = pd.DataFrame(data)

print(df)
print("---------DateTime---------")
df["invoice_date"] = pd.to_datetime(df["invoice_date"])
print("---------Date---------")
df["data"]=df["invoice_date"].dt.day
print(df["data"])
print("---------Month---------")
df["month"]=df["invoice_date"].dt.month
print(df["month"])
print("---------Year---------")
df["year"]=df["invoice_date"].dt.year
print(df["year"])






print("---------Weekday---------")
df["weekday"]=df["invoice_date"].dt.weekday
print(df["weekday"])
print("---------Week---------")
df["week"]=df["weekday"].apply(lambda x: "Weekday" if x<=5 else "Weekend")
print(df["week"])
print("---------Groupby---------")
df["group"]=df.groupby("month")["amount"].sum()
print(df["group"])
print("---------Update---------")
print(df)


print("---------DateTime Format---------")
today=pd.Timestamp.today()  
print("---------Today---------")
print(today)



df["Days_Working"]=(today - df["invoice_date"]).dt.days
print(df["Days_Working"])


#-----------------------Common Format Codes---------------
# | Code | Meaning        | Example |
# | ---- | -------------- | ------- |
# | `%Y` | Year           | 2025    |
# | `%y` | Short Year     | 25      |
# | `%m` | Month Number   | 01      |
# | `%b` | Short Month    | Jan     |
# | `%B` | Full Month     | January |
# | `%d` | Day            | 15      |
# | `%A` | Full Day Name  | Monday  |
# | `%a` | Short Day      | Mon     |
# | `%H` | Hour (24-hour) | 14      |
# | `%I` | Hour (12-hour) | 02      |
# | `%M` | Minutes        | 45      |
# | `%S` | Seconds        | 30      |

#----------------.dt Properties------------------
# | Task                       | Code                                            | Output Example        |
# | -------------------------- | ----------------------------------------------- | --------------------- |
# | Convert string to datetime | `pd.to_datetime(df["Date"])`                    | `datetime64[ns]`      |
# | Check data type            | `df.dtypes`                                     | `datetime64[ns]`      |
# | Current date & time        | `pd.Timestamp.today()`                          | `2026-08-05 18:45:00` |
# | Current date only          | `pd.Timestamp.today().date()`                   | `2026-08-05`          |
# | Year                       | `df["Date"].dt.year`                            | `2025`                |
# | Month Number               | `df["Date"].dt.month`                           | `8`                   |
# | Month Name                 | `df["Date"].dt.month_name()`                    | `August`              |
# | Day of Month               | `df["Date"].dt.day`                             | `5`                   |
# | Day Name                   | `df["Date"].dt.day_name()`                      | `Wednesday`           |
# | Hour                       | `df["Date"].dt.hour`                            | `14`                  |
# | Minute                     | `df["Date"].dt.minute`                          | `30`                  |
# | Second                     | `df["Date"].dt.second`                          | `45`                  |
# | Quarter                    | `df["Date"].dt.quarter`                         | `3`                   |
# | Weekday Number             | `df["Date"].dt.weekday`                         | `2` (Wednesday)       |
# | Week of Year               | `df["Date"].dt.isocalendar().week`              | `32`                  |
# | Format Date                | `df["Date"].dt.strftime("%d-%b-%Y")`            | `05-Aug-2025`         |
# | Date Difference            | `(df["End"]-df["Start"]).dt.days`               | `25`                  |
# | Days Since Today           | `(pd.Timestamp.today()-df["Date"]).dt.days`     | `500`                 |
# | Sort Dates                 | `df.sort_values("Date")`                        | Ascending             |
# | Sort Descending            | `df.sort_values("Date", ascending=False)`       | Descending            |
# | Filter After Date          | `df[df["Date"]>"2025-01-01"]`                   | Matching rows         |
# | Filter Before Date         | `df[df["Date"]<"2025-01-01"]`                   | Matching rows         |
# | Filter by Year             | `df[df["Date"].dt.year==2025]`                  | Matching rows         |
# | Filter by Month            | `df[df["Date"].dt.month==8]`                    | August rows           |
# | Filter by Day              | `df[df["Date"].dt.day==15]`                     | Day = 15              |
# | Date Range                 | `pd.date_range("2025-01-01","2025-01-10")`      | DateIndex             |
# | Read CSV as Date           | `pd.read_csv("file.csv", parse_dates=["Date"])` | Auto datetime         |
# | Handle Invalid Dates       | `pd.to_datetime(df["Date"], errors="coerce")`   | Invalid → `NaT`       |
# | Specify Input Format       | `pd.to_datetime(df["Date"], format="%d/%m/%Y")` | Faster conversion     |

#-----------------Most Important Functions (Exam/Interview)


# | Function               | Purpose                      |
# | ---------------------- | ---------------------------- |
# | `pd.to_datetime()`     | Convert text to datetime     |
# | `pd.Timestamp.today()` | Current timestamp            |
# | `pd.date_range()`      | Generate a sequence of dates |
# | `.dt.year`             | Extract year                 |
# | `.dt.month`            | Extract month                |
# | `.dt.day`              | Extract day                  |
# | `.dt.day_name()`       | Get weekday name             |
# | `.dt.month_name()`     | Get month name               |
# | `.dt.strftime()`       | Format datetime as text      |
# | `.sort_values()`       | Sort by date                 |
# | `parse_dates`          | Read dates directly from CSV |
