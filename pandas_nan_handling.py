import pandas as pd
import numpy as np
data = {
    "Name":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', "J"],
    "Age": [12, 45, 23, 67, 12, 67, 76, 43, 76, np.nan], 
    "Salary": [1200, 34509, 65409, 1234, 9575, 543, 432, 345, 234, np.nan]
}

df = pd.DataFrame(data)
print(df)

#checking for missing values
print("Checking for missing values")
print(df.isnull().sum())
print(df)
#drop missing values
df.dropna(inplace=True)
print(df)

#fill the missing values
df.fillna(0, inplace=True)
print(df)

#dropping using axis
df.dropna(axis=0, inplace=True)
print(df)

#filling for specific values of a col
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df)

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)

a = df['Age'].value_counts()
print(a)