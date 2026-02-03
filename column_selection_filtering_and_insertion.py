import pandas as pd

data = {
    "Name":['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    "Age": [12, 45, 23, 67, 12, 67, 76, 43, 76], 
    "Salary": [1200, 34509, 65409, 1234, 9575, 543, 432, 345, 234],
}

df = pd.DataFrame(data)
print(df)
df.to_excel("Original.xlsx", index=False)
#selecting single col
print("___________________________________")
col = df['Name']
print(col)

print("selecting multi col")

mult_col = df[["Name", "Age"]]
print(mult_col) 

print("filtering on one condition")

filter_row = df[df["Age"] == 67]
print(filter_row)

print("filter on two condition using &")

mult_row_filter = df[(df["Age"] == 43) & (df['Salary'] > 100)]
print(mult_row_filter)

print("filter on two condition using |")
mult_or = df[(df["Age"] == 67) | (df['Salary'] > 8900)]
print(mult_or)

print("Adding a new col at specific position")
df.insert(0, "ID", [f"E_{i}" for i in range(101, 110)])
print(df)

df.to_excel("modified.xlsx", index=False)