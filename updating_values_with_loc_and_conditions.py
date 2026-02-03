import pandas as pd

data = {
    "Name":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    "Age": [12, 45, 23, 67, 12, 67, 76, 43, 76], 
    "Salary": [1200, 34509, 65409, 1234, 9575, 543, 432, 345, 234],
}

df = pd.DataFrame(data)
print(df)

#updating the salary of D

df.loc[2, "Salary"] = 2345
print(df)

print("Original_Data")
print(df)

df['Salary'] = df['Salary'] *1.05
print("Modifed data")
print(df)

#dropping the col
#df.drop(columns=["Name"], inplace=True)
print(df)

#cleaner drop

df.loc[df['Name'] == 'D', "Salary"] = 7656
print(df)