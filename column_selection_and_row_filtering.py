import pandas as pd

df = pd.read_csv('iris.csv')

#selecting a single column

selected_col = df['SepalLength Cm']
print(selected_col)

#multiple col

mult_col = df[['SepalLength Cm','SepalWidth Cm']]
print(mult_col)

#filter

row_filter = df[df['SepalLength Cm'] == 5.1]
print(row_filter)

#filtring of more than one features

filter_row = df[(df['SepalLength Cm'] == 5.1) & (df['SepalWidth Cm'] == 3.5)]
print(filter_row)

filter_or = df[(df['SepalLength Cm'] == 5.1) | (df['SepalWidth Cm'] == 3.5)]
print(filter_or)