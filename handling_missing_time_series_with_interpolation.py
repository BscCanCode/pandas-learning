import pandas as pd
import numpy as np

data = {
    "Date": [
        "2024-01-01", "2024-02-01",np.nan, "2024-03-01", "2024-04-01",
        "2024-05-01",np.nan, "2024-06-01", "2024-07-01", "2024-08-01",
        "2024-09-01", "2024-10-01", np.nan
    ],
    "Sales": [100, np.nan, 120, 140, 160, 180,np.nan, 200, 220, 240,np.nan, 260, 280]
}
print("Reading a dataframe")
df = pd.DataFrame(data)
print(df)
print()
print("Counting missing values")
#count missing values
print(df.isnull().sum())

#drop missing dates
df = df.dropna(subset=['Date'])
print(df)

df['Date'] = pd.to_datetime(df['Date'])
df.sort_values("Date")
print(df)
#Handling missing values using interploation for sales
df['Sales'] = df['Sales'].interpolate(method="linear")
print(df)