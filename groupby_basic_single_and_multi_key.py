import pandas as pd

data = {
    "Name": ['Z', 'D', 'C', 'Q', 'A'],
    "Age" : [12, 90, 54, 45, 34],
    "Salary":[5545, 865, 6434, 64, 45]
}

df = pd.DataFrame(data)
print(df)

#single grouping
grouped = df.groupby('Age')['Salary'].sum()
print(grouped)

#multiple col group

group = df.groupby(['Name', 'Age'])['Salary'].sum()
print(group)