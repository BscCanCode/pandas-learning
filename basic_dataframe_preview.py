import pandas as pd

df = pd.read_csv('iris.csv')

#prints top 5 records
print(df.head())

print("------------------------------------------------------")

#prints bottom 5 records
print(df.tail())