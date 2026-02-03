import pandas as pd

data = {
    "Name": ['Z', 'D', 'C', 'Q', 'A'],
    "Age" : [12, 90, 54, 45, 34],
    "Salary":[5545, 865, 6434, 64, 45]
}

df = pd.DataFrame(data)
print(df)

#sorting one column
df = df.sort_values(by='Name', ascending=False)
print(df)

#sorting multiple column
df = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
print(df)